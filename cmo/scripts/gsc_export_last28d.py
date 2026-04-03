#!/usr/bin/env python3
"""Export Google Search Console last-28d Search Analytics to CSV.

Autonomous, evidence-first: lists accessible properties, then exports
(top queries + top pages) for a chosen site.

Safe-by-default:
- Reads SA JSON from a secrets mount (default: /root/moxie/secrets/google-service-account.json)
- Does NOT print private_key

Usage examples:
  source /root/moxie_hq/.venv-moxie/bin/activate
  python3 cmo/scripts/gsc_export_last28d.py --site https://formbeep.com/

Outputs:
  <out_dir>/gsc_queries_last28d.csv
  <out_dir>/gsc_pages_last28d.csv
  <out_dir>/gsc_export_meta.json
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

DEFAULT_SA_PATHS = [
    "/root/moxie/secrets/google-service-account.json",
    "/root/moxie_secrets/google-service-account.json",
]


@dataclass
class ExportMeta:
    generated_utc: str
    site: str
    date_start: str
    date_end: str
    rows_queries: int
    rows_pages: int


def _utc_today_iso() -> str:
    # Good enough for metadata; avoids adding deps.
    return str(date.today())


def resolve_sa_path(p: Optional[str]) -> Path:
    if p:
        path = Path(p)
        if not path.exists():
            raise FileNotFoundError(f"Service account JSON not found: {path}")
        return path

    for candidate in DEFAULT_SA_PATHS:
        path = Path(candidate)
        if path.exists():
            return path

    raise FileNotFoundError(
        "No service account JSON found. Looked in: " + ", ".join(DEFAULT_SA_PATHS)
    )


def gsc_client(sa_path: Path):
    creds = service_account.Credentials.from_service_account_file(
        str(sa_path), scopes=SCOPES
    )
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def list_sites(service) -> List[str]:
    resp = service.sites().list().execute()
    sites = []
    for e in resp.get("siteEntry", []) or []:
        site_url = e.get("siteUrl")
        perm = e.get("permissionLevel")
        if site_url and perm and perm != "siteUnverifiedUser":
            sites.append(site_url)
    return sorted(set(sites))


def export_dimension(service, site: str, dimension: str, start: str, end: str, row_limit: int = 5000) -> List[Dict[str, Any]]:
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": [dimension],
        "rowLimit": row_limit,
    }
    resp = service.searchanalytics().query(siteUrl=site, body=body).execute()
    rows = resp.get("rows", []) or []
    out = []
    for r in rows:
        keys = r.get("keys", []) or []
        out.append(
            {
                dimension: keys[0] if keys else "",
                "clicks": r.get("clicks", 0),
                "impressions": r.get("impressions", 0),
                "ctr": r.get("ctr", 0),
                "position": r.get("position", 0),
            }
        )
    return out


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True, help="GSC siteUrl (e.g. https://formbeep.com/ or sc-domain:formbeep.com)")
    ap.add_argument("--sa", default=None, help="Path to service account JSON (optional)")
    ap.add_argument("--out_dir", default=None, help="Output directory (default: products/<site>/analytics/inputs)")
    ap.add_argument("--days", type=int, default=28)
    args = ap.parse_args()

    sa_path = resolve_sa_path(args.sa)
    service = gsc_client(sa_path)

    # Verify access up-front.
    sites = list_sites(service)
    if args.site not in sites:
        raise SystemExit(
            "Requested site not accessible via this service account.\n"
            f"Requested: {args.site}\n"
            "Accessible sites:\n- " + "\n- ".join(sites)
        )

    end_d = date.today() - timedelta(days=1)
    start_d = end_d - timedelta(days=args.days - 1)
    start = start_d.isoformat()
    end = end_d.isoformat()

    # Infer default out_dir if not set.
    out_dir = Path(args.out_dir) if args.out_dir else None
    if out_dir is None:
        # conservative: write under /root/moxie/products/formbeep/analytics/inputs when site contains formbeep
        if "formbeep" in args.site:
            out_dir = Path("/root/moxie/products/formbeep/analytics/inputs")
        elif "stackstats" in args.site:
            out_dir = Path("/root/moxie/products/stackstats/analytics/inputs")
        else:
            out_dir = Path("/root/moxie/products/_meta/analytics/inputs") / args.site.replace(":", "_").replace("/", "_")

    q_rows = export_dimension(service, args.site, "query", start, end)
    p_rows = export_dimension(service, args.site, "page", start, end)

    write_csv(out_dir / "gsc_queries_last28d.csv", q_rows, ["query", "clicks", "impressions", "ctr", "position"])
    write_csv(out_dir / "gsc_pages_last28d.csv", p_rows, ["page", "clicks", "impressions", "ctr", "position"])

    meta = ExportMeta(
        generated_utc=_utc_today_iso(),
        site=args.site,
        date_start=start,
        date_end=end,
        rows_queries=len(q_rows),
        rows_pages=len(p_rows),
    )
    (out_dir / "gsc_export_meta.json").write_text(json.dumps(asdict(meta), indent=2), encoding="utf-8")

    print(str(out_dir))
    print(f"queries_rows={len(q_rows)}")
    print(f"pages_rows={len(p_rows)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except HttpError as e:
        # Print minimal diagnostics without leaking creds.
        print("GSC_HTTP_ERROR", getattr(e, 'status_code', None) or "", str(e))
        raise
