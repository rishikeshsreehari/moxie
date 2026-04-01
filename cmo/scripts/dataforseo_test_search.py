"""DataForSEO test search (SAFE MODE by default).

Rules:
- DO NOT spend credits without explicit approval.
- By default this script only validates that we can build the request.
- To actually run a query, pass --run and confirm you have approval.

Reads credentials from:
- /root/moxie_secrets/dataforseo_basic_auth.txt  (preferred)

Outputs:
- Prints request payload and (if --run) saves response to an output JSON.

"""

import argparse
import base64
import json
import os
import re
from datetime import datetime
from urllib.request import Request, urlopen

# Secret file is not committed to git; see:
#   /root/moxie_hq/cmo/resources/credentials/dataforseo.md
DEFAULT_SECRET_FILE = os.getenv(
    "DATAFORSEO_BASIC_AUTH_FILE",
    "/root/moxie_secrets/dataforseo_basic_auth.txt",
)


def load_basic_auth(secret_file: str = DEFAULT_SECRET_FILE) -> str:
    txt = open(secret_file, "r", encoding="utf-8").read()
    # Try to find base64 line
    m = re.search(r"^a[A-Za-z0-9+/=]+$", txt, re.M)
    if m:
        b64 = m.group(0).strip()
        return b64
    # Else derive from login:password line
    m = re.search(r"^(\S+@\S+):(\S+)$", txt, re.M)
    if not m:
        raise RuntimeError("Could not find credentials in secret file")
    raw = f"{m.group(1)}:{m.group(2)}".encode("utf-8")
    return base64.b64encode(raw).decode("ascii")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keyword", required=True)
    ap.add_argument("--location_code", type=int, default=2840, help="US default")
    ap.add_argument("--language_code", default="en")

    # SAFE MODE is default. The API call only occurs with --run AND --approved.
    ap.add_argument("--run", action="store_true", help="Actually call the API (spends credits)")
    ap.add_argument(
        "--approved",
        action="store_true",
        help="Set ONLY after explicit Rishi approval (required with --run)",
    )

    ap.add_argument(
        "--secret_file",
        default=DEFAULT_SECRET_FILE,
        help="Path to Basic Auth secret file (default: $DATAFORSEO_BASIC_AUTH_FILE or /root/moxie_secrets/dataforseo_basic_auth.txt)",
    )
    ap.add_argument("--out", default="/root/moxie/products/formbeep/seo/dataforseo-test-response.json")
    args = ap.parse_args()

    b64 = load_basic_auth(args.secret_file)

    # NOTE: Endpoint/path must be confirmed from DataForSEO docs before --run.
    # Placeholder endpoint to be filled by the assignee after reading docs.
    endpoint = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"

    payload = [{
        "keyword": args.keyword,
        "location_code": args.location_code,
        "language_code": args.language_code,
        "device": "desktop",
        "os": "windows",
        "depth": 10,
    }]

    print("SAFE MODE: request prepared")
    print("Endpoint:", endpoint)
    print("Payload:", json.dumps(payload, indent=2))

    if not args.run:
        print("Not running. SAFE MODE active.")
        print("To run (spends credits): pass --run --approved ONLY after explicit Rishi approval.")
        return

    if not args.approved:
        raise SystemExit("Refusing to run without --approved (requires explicit Rishi approval).")

    # Running: do the API call
    req = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Basic {b64}",
            "Content-Type": "application/json",
            "User-Agent": "moxie-serp-test",
        },
        method="POST",
    )

    with urlopen(req, timeout=60) as r:
        body = r.read().decode("utf-8", errors="replace")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(body)

    print("Saved response to", args.out)


if __name__ == "__main__":
    main()
