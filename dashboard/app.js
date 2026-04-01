/* Public-safe dashboard renderer.
   Reads ./public_snapshot.json (sanitized). If missing, falls back to sample.
*/

const SAMPLE = {
  generated_at: "2026-04-01T00:00:00Z",
  kpis: {
    pageviews_7d: 103,
    visitors_7d: 76,
    signups_7d: 4,
    paid_7d: 0
  },
  products: [
    { name: "FormBeep", status: "active", pageviews_7d: 103, signups_7d: 4 }
  ],
  systems: {
    queue: { pending: 0, in_progress: 0 },
    blockers: { count: 6 },
    cron: { active_jobs: 19, note: "local-only outputs" }
  },
  team: [
    { role: "Moxie (Autonomous CMO)", status: "ACTIVE", focus: "Orchestration + decisions" },
    { role: "Growth Research", status: "IN_PROGRESS", focus: "Demand probes + keyword roadmap" },
    { role: "Outreach", status: "BLOCKED", focus: "Needs social creds" },
    { role: "Distribution Ops", status: "BLOCKED", focus: "Needs directory inbox access" },
    { role: "Conversion Copy", status: "IDLE", focus: "Drafts ready" },
    { role: "Analytics", status: "BLOCKED", focus: "API access restricted" },
    { role: "Partnerships", status: "BLOCKED", focus: "Portal access pending" },
    { role: "Outbound", status: "IDLE", focus: "Pack ready" },
    { role: "Competitor Intel", status: "IDLE", focus: "Monthly scan done" }
  ],
  console: [
    "[OK] Snapshot loaded (sanitized)",
    "[INFO] Jobs: 19 active (local outputs)",
    "[WARN] Some execution is blocked on credentials",
    "[NOTE] This page never shows emails, tokens, IDs, referrers, or customer data"
  ]
};

function fmtDate(iso) {
  try {
    const d = new Date(iso);
    return d.toLocaleString();
  } catch {
    return iso;
  }
}

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function statusBadge(status) {
  const s = (status || "").toUpperCase();
  // Keep it simple: text only (monochrome)
  return s || "—";
}

function renderTeam(team) {
  const tbody = document.getElementById("teamRows");
  if (!tbody) return;
  tbody.innerHTML = "";

  team.forEach(row => {
    const tr = document.createElement("tr");
    const tdRole = document.createElement("td");
    const tdStatus = document.createElement("td");
    const tdFocus = document.createElement("td");

    tdRole.textContent = row.role;
    tdStatus.textContent = statusBadge(row.status);
    tdFocus.textContent = row.focus || "";

    tr.appendChild(tdRole);
    tr.appendChild(tdStatus);
    tr.appendChild(tdFocus);
    tbody.appendChild(tr);
  });
}

function renderProducts(products) {
  const tbody = document.getElementById("productRows");
  if (!tbody) return;
  tbody.innerHTML = "";

  products.forEach(p => {
    const tr = document.createElement("tr");
    const tdName = document.createElement("td");
    const tdStatus = document.createElement("td");
    const tdPv = document.createElement("td");
    const tdSignups = document.createElement("td");

    tdName.textContent = p.name;
    tdStatus.textContent = statusBadge(p.status);
    tdPv.textContent = String(p.pageviews_7d ?? "—");
    tdSignups.textContent = String(p.signups_7d ?? "—");

    tr.appendChild(tdName);
    tr.appendChild(tdStatus);
    tr.appendChild(tdPv);
    tr.appendChild(tdSignups);
    tbody.appendChild(tr);
  });
}

function renderConsole(lines) {
  const el = document.getElementById("consoleText");
  if (!el) return;
  el.textContent = (lines || []).join("\n");
}

function nodeStyle(status) {
  // SVG node style variants in monochrome
  const s = (status || "").toUpperCase();
  if (s === "BLOCKED") return { strokeDasharray: "8 6", fill: "#fff" };
  if (s === "IN_PROGRESS") return { strokeDasharray: "2 2", fill: "#fff" };
  if (s === "ACTIVE") return { strokeDasharray: "0", fill: "#fff" };
  return { strokeDasharray: "0", fill: "#fff", opacity: 0.75 };
}

function renderDiagram(team) {
  const edges = document.getElementById("edges");
  const nodes = document.getElementById("nodes");
  if (!edges || !nodes) return;
  edges.innerHTML = "";
  nodes.innerHTML = "";

  // Layout: center = Moxie; ring of roles.
  const cx = 400, cy = 220;
  const center = { label: "MOXIE", status: "ACTIVE" };

  // pick up to 10 roles (excluding moxie if present)
  const roles = (team || []).filter(r => !String(r.role || "").toLowerCase().includes("moxie")).slice(0, 10);

  // draw center
  drawNode(nodes, cx, cy, 150, 46, center.label, center.status);

  const radius = 185;
  const startAngle = -Math.PI / 2;
  const step = roles.length ? (2 * Math.PI) / roles.length : 0;

  roles.forEach((r, i) => {
    const a = startAngle + i * step;
    const x = cx + Math.cos(a) * radius;
    const y = cy + Math.sin(a) * radius;

    drawEdge(edges, cx, cy, x, y, r.status);
    drawNode(nodes, x, y, 170, 44, (r.role || "ROLE").toUpperCase(), r.status);
  });

  // Add a small bottom "HQ" node
  const hx = 400, hy = 380;
  drawEdge(edges, cx, cy, hx, hy, "ACTIVE");
  drawNode(nodes, hx, hy, 120, 40, "HQ", "ACTIVE");
}

function drawEdge(parent, x1, y1, x2, y2, status) {
  const s = (status || "").toUpperCase();
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  const midx = (x1 + x2) / 2;
  const midy = (y1 + y2) / 2;
  // subtle curve
  const dx = (x2 - x1) * 0.15;
  const dy = (y2 - y1) * 0.15;
  path.setAttribute("d", `M ${x1} ${y1} Q ${midx + dy} ${midy - dx} ${x2} ${y2}`);
  path.setAttribute("stroke", "#111");
  path.setAttribute("stroke-width", "2");
  path.setAttribute("fill", "none");

  if (s === "BLOCKED") path.setAttribute("stroke-dasharray", "10 7");
  else if (s === "IN_PROGRESS") path.setAttribute("stroke-dasharray", "3 3");

  parent.appendChild(path);
}

function drawNode(parent, x, y, w, h, label, status) {
  const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

  const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  rect.setAttribute("x", x - w / 2);
  rect.setAttribute("y", y - h / 2);
  rect.setAttribute("rx", "8");
  rect.setAttribute("ry", "8");
  rect.setAttribute("width", w);
  rect.setAttribute("height", h);
  rect.setAttribute("stroke", "#111");
  rect.setAttribute("stroke-width", "2");

  const style = nodeStyle(status);
  if (style.strokeDasharray && style.strokeDasharray !== "0") rect.setAttribute("stroke-dasharray", style.strokeDasharray);
  rect.setAttribute("fill", style.fill || "#fff");
  if (style.opacity) rect.setAttribute("opacity", String(style.opacity));

  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", x);
  text.setAttribute("y", y + 4);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("font-size", "13");
  text.setAttribute("fill", "#111");
  text.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  text.textContent = label;

  g.appendChild(rect);
  g.appendChild(text);
  parent.appendChild(g);
}

function applySnapshot(snap) {
  setText("generatedAt", `Snapshot: ${fmtDate(snap.generated_at || "")}`);

  setText("kpiPv", snap.kpis?.pageviews_7d ?? "—");
  setText("kpiVisitors", snap.kpis?.visitors_7d ?? "—");
  setText("kpiSignups", snap.kpis?.signups_7d ?? "—");
  setText("kpiPaid", snap.kpis?.paid_7d ?? "—");

  const active = (snap.products || []).find(p => String(p.status).toLowerCase() === "active") || (snap.products || [])[0];
  setText("activeProduct", active ? active.name : "—");

  const q = snap.systems?.queue;
  setText("queueState", q ? `${q.in_progress} in progress • ${q.pending} pending` : "—");

  setText("blockerCount", snap.systems?.blockers?.count ?? "—");

  renderTeam(snap.team || []);
  renderProducts(snap.products || []);
  renderConsole(snap.console || []);
  renderDiagram(snap.team || []);
}

async function load() {
  try {
    const res = await fetch("./public_snapshot.json", { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const snap = await res.json();
    applySnapshot(snap);
  } catch (e) {
    // fallback
    const lines = [...SAMPLE.console, `[FALLBACK] Could not load public_snapshot.json (${e.message})`];
    applySnapshot({ ...SAMPLE, console: lines });
  }
}

load();
