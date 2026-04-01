/*
  Moxie HQ Dashboard
  - Static site
  - Reads ./public_snapshot.json
  - Adds light animation so it feels live
*/

const SAMPLE = {
  generated_at: "2026-04-01T00:00:00Z",
  kpis: {
    pageviews_7d: 103,
    visitors_7d: 76,
    signups_7d: 4,
    paid_7d: 0,
    mrr_usd: 0,
    revenue_total_usd: 0
  },
  products: [
    { name: "FormBeep", status: "ACTIVE", pageviews_7d: 103, signups_7d: 4 }
  ],
  systems: {
    queue: { pending: 0, in_progress: 0 },
    blockers: {
      count: 6,
      needs_rishi: [
        "Directory inbox access",
        "Reddit credentials",
        "Marketplace portals access",
        "Approve SEO fixes",
        "Review blog drafts"
      ]
    }
  },
  running: {
    count: 3,
    tasks: [
      { role: "SERP Research", status: "IN_PROGRESS", text: "US SERP analysis in progress" },
      { role: "Competitor Intel", status: "DONE", text: "Competitor scan done (3 insights)" },
      { role: "Directories", status: "WAITING", text: "Waiting on founder to submit 2 planned directories" }
    ],
    highlights: [
      "Reddit competitor analysis: done",
      "US SERP analysis: in progress",
      "Directory submissions: waiting on founder"
    ]
  },
  team: [
    { role: "Moxie", status: "ACTIVE", working_on: "Orchestration + decisions" },
    { role: "Astra (Growth Research)", status: "IN_PROGRESS", working_on: "SERP demand probe" },
    { role: "Ember (Outreach)", status: "BLOCKED", working_on: "Reddit posting (needs creds)" },
    { role: "Jax (Distribution Ops)", status: "BLOCKED", working_on: "Directories (needs inbox)" },
    { role: "Forge (SEO)", status: "WAITING", working_on: "Implementation pending approval" },
    { role: "Kiro (Copy)", status: "WAITING", working_on: "Blog drafts pending review" },
    { role: "Pax (Partnerships)", status: "BLOCKED", working_on: "Portals access pending" },
    { role: "Mira (Analytics)", status: "BLOCKED", working_on: "API access restricted" },
    { role: "Vale (Competitor Intel)", status: "DONE", working_on: "Monthly scan complete" }
  ],
  github: {
    recent: [
      { hash: "acb9687", when: "2026-04-01", subject: "Add public retro HQ dashboard" },
      { hash: "574703c", when: "2026-04-01", subject: "Framework: replication rules + checklists" }
    ]
  },
  console: [
    "[BOOT] Moxie HQ online",
    "[SYNC] reading orchestration state",
    "[RUN ] workers scheduled (local)",
    "[WAIT] some execution requires founder action"
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

function clampStr(s, n = 90) {
  const t = String(s || "");
  return t.length > n ? t.slice(0, n - 1) + "…" : t;
}

function statusNorm(s) {
  const x = String(s || "").toUpperCase();
  if (["ACTIVE","IN_PROGRESS","BLOCKED","IDLE","DONE","WAITING"].includes(x)) return x;
  return x || "—";
}

function renderTeam(team) {
  const tbody = document.getElementById("teamRows");
  if (!tbody) return;
  tbody.innerHTML = "";

  (team || []).forEach(row => {
    const tr = document.createElement("tr");
    const tdRole = document.createElement("td");
    const tdStatus = document.createElement("td");
    const tdWork = document.createElement("td");

    tdRole.textContent = row.role;
    tdStatus.textContent = statusNorm(row.status);
    tdWork.textContent = clampStr(row.working_on || row.focus || "");

    tr.appendChild(tdRole);
    tr.appendChild(tdStatus);
    tr.appendChild(tdWork);
    tbody.appendChild(tr);
  });
}

function renderProducts(products) {
  const tbody = document.getElementById("productRows");
  if (!tbody) return;
  tbody.innerHTML = "";

  (products || []).forEach(p => {
    const tr = document.createElement("tr");
    const tdName = document.createElement("td");
    const tdStatus = document.createElement("td");
    const tdPv = document.createElement("td");
    const tdSignups = document.createElement("td");

    tdName.textContent = p.name;
    tdStatus.textContent = statusNorm(p.status);
    tdPv.textContent = String(p.pageviews_7d ?? "—");
    tdSignups.textContent = String(p.signups_7d ?? "—");

    tr.appendChild(tdName);
    tr.appendChild(tdStatus);
    tr.appendChild(tdPv);
    tr.appendChild(tdSignups);
    tbody.appendChild(tr);
  });
}

function renderList(id, items, empty = "—") {
  const ul = document.getElementById(id);
  if (!ul) return;
  ul.innerHTML = "";
  const arr = (items || []).filter(Boolean);
  if (!arr.length) {
    const li = document.createElement("li");
    li.textContent = empty;
    ul.appendChild(li);
    return;
  }
  arr.slice(0, 8).forEach(x => {
    const li = document.createElement("li");
    li.textContent = clampStr(x, 110);
    ul.appendChild(li);
  });
}

function renderOpsTasks(tasks) {
  const ul = document.getElementById("opsTasks");
  if (!ul) return;
  ul.innerHTML = "";

  const arr = tasks || [];
  if (!arr.length) {
    const li = document.createElement("li");
    li.textContent = "No active work items.";
    ul.appendChild(li);
    return;
  }

  arr.slice(0, 6).forEach(t => {
    const li = document.createElement("li");
    const s = statusNorm(t.status);
    li.textContent = `[${s}] ${t.role ? t.role + ": " : ""}${t.text || ""}`;
    ul.appendChild(li);
  });
}

function renderGitHub(recent) {
  const ul = document.getElementById("githubList");
  if (!ul) return;
  ul.innerHTML = "";

  const arr = recent || [];
  if (!arr.length) {
    const li = document.createElement("li");
    li.textContent = "No commits found.";
    ul.appendChild(li);
    return;
  }

  arr.slice(0, 7).forEach(c => {
    const li = document.createElement("li");
    li.textContent = `${c.when || ""}  ${c.hash || ""}  ${c.subject || ""}`.trim();
    ul.appendChild(li);
  });
}

function renderConsoleAnimated(lines) {
  const el = document.getElementById("consoleText");
  if (!el) return;

  const caret = "<span class=\"caret\">▌</span>";
  const arr = (lines || []).slice(0, 24);

  // typewriter-ish: reveal one line per 140ms, then loop quietly
  el.innerHTML = "";
  let i = 0;

  function tick() {
    if (i < arr.length) {
      const safe = escapeHtml(arr[i]);
      el.innerHTML += safe + "\n";
      i += 1;
    }
    el.innerHTML = el.innerHTML.replace(/<span class=\\"caret\\">▌<\\/span>$/g, "");
    el.innerHTML += caret;
    if (i <= arr.length) setTimeout(tick, 140);
  }

  tick();
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\"/g, "&quot;");
}

function nodeClass(status) {
  const s = statusNorm(status);
  if (s === "BLOCKED") return "node blocked";
  if (s === "IN_PROGRESS") return "node progress";
  if (s === "ACTIVE") return "node active";
  if (s === "DONE") return "node done";
  if (s === "WAITING") return "node waiting";
  return "node idle";
}

function edgeClass(status) {
  const s = statusNorm(status);
  if (s === "BLOCKED") return "edge blocked";
  if (s === "IN_PROGRESS") return "edge progress";
  if (s === "ACTIVE") return "edge active";
  if (s === "DONE") return "edge done";
  if (s === "WAITING") return "edge waiting";
  return "edge idle";
}

function renderDiagram(snapshot) {
  const edges = document.getElementById("edges");
  const nodes = document.getElementById("nodes");
  if (!edges || !nodes) return;
  edges.innerHTML = "";
  nodes.innerHTML = "";

  const team = snapshot.team || [];
  const products = snapshot.products || [];

  // center
  const cx = 450, cy = 250;
  drawNode(nodes, cx, cy, 190, 58, "MOXIE", "ACTIVE", "autonomous CMO");

  // ring roles
  const roles = team
    .filter(r => !String(r.role || "").toLowerCase().startsWith("moxie"))
    .slice(0, 12);

  const radius = 210;
  const start = -Math.PI / 2;
  const step = roles.length ? (2 * Math.PI) / roles.length : 0;

  roles.forEach((r, i) => {
    const a = start + i * step;
    const x = cx + Math.cos(a) * radius;
    const y = cy + Math.sin(a) * radius;

    drawEdge(edges, cx, cy, x, y, r.status);

    const label = String(r.role || "ROLE").replace(/\s*\(.*\)\s*/g, "");
    const sub = clampStr(r.working_on || "", 26);
    drawNode(nodes, x, y, 210, 56, label.toUpperCase(), r.status, sub);
  });

  // product nodes under
  const py = 455;
  const startX = 290;
  const gap = 160;

  products.slice(0, 4).forEach((p, i) => {
    const x = startX + i * gap;
    drawEdge(edges, cx, cy + 20, x, py, "ACTIVE");
    drawNode(nodes, x, py, 150, 44, String(p.name || "PRODUCT").toUpperCase(), p.status, "active");
  });

  // animate edges by adding a moving dash offset loop
  animateSvgEdges();
}

let _edgeAnimStarted = false;
function animateSvgEdges() {
  if (_edgeAnimStarted) return;
  _edgeAnimStarted = true;

  let t = 0;
  const edges = document.querySelectorAll("#edges path");

  function frame() {
    t += 1;
    edges.forEach((p, idx) => {
      const cls = p.getAttribute("class") || "";
      let speed = 0.0;
      if (cls.includes("progress")) speed = 1.4;
      else if (cls.includes("active")) speed = 0.8;
      else if (cls.includes("blocked")) speed = 0.2;
      else speed = 0.35;
      p.style.strokeDashoffset = String((t * speed + idx * 3) % 200);
    });
    requestAnimationFrame(frame);
  }

  requestAnimationFrame(frame);
}

function drawEdge(parent, x1, y1, x2, y2, status) {
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");

  const midx = (x1 + x2) / 2;
  const midy = (y1 + y2) / 2;
  const dx = (x2 - x1) * 0.15;
  const dy = (y2 - y1) * 0.15;

  path.setAttribute("d", `M ${x1} ${y1} Q ${midx + dy} ${midy - dx} ${x2} ${y2}`);
  path.setAttribute("stroke", "#111");
  path.setAttribute("stroke-width", "2");
  path.setAttribute("fill", "none");
  path.setAttribute("class", edgeClass(status));

  const s = statusNorm(status);
  if (s === "BLOCKED") path.setAttribute("stroke-dasharray", "12 9");
  else if (s === "IN_PROGRESS") path.setAttribute("stroke-dasharray", "4 4");
  else path.setAttribute("stroke-dasharray", "2 10");

  parent.appendChild(path);
}

function drawNode(parent, x, y, w, h, label, status, subline = "") {
  const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
  g.setAttribute("class", nodeClass(status));

  const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  rect.setAttribute("x", x - w / 2);
  rect.setAttribute("y", y - h / 2);
  rect.setAttribute("rx", "10");
  rect.setAttribute("ry", "10");
  rect.setAttribute("width", w);
  rect.setAttribute("height", h);
  rect.setAttribute("stroke", "#111");
  rect.setAttribute("stroke-width", "2");
  rect.setAttribute("fill", "#fff");

  const s = statusNorm(status);
  if (s === "BLOCKED") rect.setAttribute("stroke-dasharray", "10 7");
  else if (s === "IN_PROGRESS") rect.setAttribute("stroke-dasharray", "3 3");

  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", x);
  text.setAttribute("y", y - 2);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("font-size", "13");
  text.setAttribute("fill", "#111");
  text.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  text.textContent = clampStr(label, 22);

  const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
  sub.setAttribute("x", x);
  sub.setAttribute("y", y + 16);
  sub.setAttribute("text-anchor", "middle");
  sub.setAttribute("font-size", "11");
  sub.setAttribute("fill", "#111");
  sub.setAttribute("opacity", "0.7");
  sub.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  sub.textContent = clampStr(subline, 28);

  g.appendChild(rect);
  g.appendChild(text);
  if (subline) g.appendChild(sub);

  parent.appendChild(g);
}

function applySnapshot(snap) {
  setText("generatedAt", `Snapshot: ${fmtDate(snap.generated_at || "")}`);

  setText("kpiPv", snap.kpis?.pageviews_7d ?? "—");
  setText("kpiVisitors", snap.kpis?.visitors_7d ?? "—");
  setText("kpiSignups", snap.kpis?.signups_7d ?? "—");
  setText("kpiPaid", snap.kpis?.paid_7d ?? "—");

  setText("kpiMrr", snap.kpis?.mrr_usd ?? 0);
  setText("kpiRevenueTotal", snap.kpis?.revenue_total_usd ?? 0);

  const active = (snap.products || []).find(p => String(p.status || "").toUpperCase() === "ACTIVE") || (snap.products || [])[0];
  setText("activeProduct", active ? active.name : "—");

  const q = snap.systems?.queue;
  setText("queueState", q ? `${q.in_progress} in progress • ${q.pending} pending` : "—");

  const runningCount = snap.running?.count ?? (snap.running?.tasks || []).length;
  setText("runningCount", runningCount ?? "—");

  setText("blockerCount", snap.systems?.blockers?.count ?? "—");

  renderTeam(snap.team || []);
  renderProducts(snap.products || []);

  renderOpsTasks(snap.running?.tasks || []);
  renderList("highlights", snap.running?.highlights || [], "—");
  renderList("blockersList", snap.systems?.blockers?.needs_rishi || [], "—");
  renderGitHub(snap.github?.recent || []);

  const baseConsole = snap.console || [];
  const extra = [];
  extra.push(`[PULSE] ${new Date().toLocaleTimeString()} heartbeat`);
  extra.push(`[STATE] running=${runningCount ?? 0} blockers=${snap.systems?.blockers?.count ?? 0}`);
  renderConsoleAnimated([...baseConsole, ...extra]);

  renderDiagram(snap);

  // footer pulse
  setText("footerPulse", `jobs:${snap.systems?.cron?.active_jobs ?? "—"}  queue:${q ? q.pending : "—"}`);
}

function tickClock() {
  setText("liveClock", new Date().toLocaleString());
}

async function load() {
  tickClock();
  setInterval(tickClock, 1000);

  try {
    const res = await fetch("./public_snapshot.json", { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const snap = await res.json();
    applySnapshot(snap);
  } catch (e) {
    applySnapshot({
      ...SAMPLE,
      console: [...SAMPLE.console, `[FALLBACK] public_snapshot.json unavailable (${e.message})`]
    });
  }
}

load();
