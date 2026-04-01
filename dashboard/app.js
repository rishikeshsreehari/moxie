/*
  Moxie HQ (public) — single-screen SCADA style.
  Reads ./public_snapshot.json and animates the network map.
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
    queue: { pending: 0, in_progress: 1 },
    cron: { active_jobs: 0 },
    blockers: {
      count: 6,
      needs_rishi: [
        "Directory inbox access / existing accounts",
        "Reddit credentials for posting",
        "Marketplace portal access",
        "Approve SEO fixes",
        "Review + publish blog drafts",
        "WP plugin resubmission"
      ]
    }
  },
  running: {
    count: 3,
    tasks: [
      { role: "Growth Research", status: "IN_PROGRESS", text: "US SERP demand probe" },
      { role: "Competitor Intel", status: "DONE", text: "Assessing competitor data: 3 insights extracted" },
      { role: "Directories", status: "WAITING", text: "Waiting on founder: execute 2 directory submissions" }
    ],
    highlights: [
      "Reddit competitor analysis: done",
      "US SERP analysis: in progress",
      "Directories: waiting on founder"
    ]
  },
  team: [
    { role: "Moxie", status: "ACTIVE", working_on: "Orchestration + decisions" },
    { role: "Astra", status: "IN_PROGRESS", working_on: "SERP demand probe" },
    { role: "Vale", status: "DONE", working_on: "Competitor scan" },
    { role: "Ember", status: "BLOCKED", working_on: "Reddit execution" },
    { role: "Jax", status: "BLOCKED", working_on: "Directories" },
    { role: "Pax", status: "BLOCKED", working_on: "Portals" },
    { role: "Forge", status: "WAITING", working_on: "SEO fixes approval" },
    { role: "Kiro", status: "WAITING", working_on: "Blog publish" }
  ],
  github: {
    recent: [
      { hash: "cbe3108", when: "2026-04-01", subject: "Dashboard improvements" }
    ]
  },
  console: [
    "[BOOT] Moxie HQ online",
    "[SYNC] reading orchestration state",
    "[RUN ] workers scheduled",
    "[WAIT] some execution requires founder actions"
  ]
};

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function fmtDate(iso) {
  try {
    return new Date(iso).toLocaleString();
  } catch {
    return iso;
  }
}

function clampStr(s, n = 110) {
  const t = String(s || "");
  return t.length > n ? t.slice(0, n - 1) + "…" : t;
}

function statusNorm(s) {
  const x = String(s || "").toUpperCase();
  if (["ACTIVE","IN_PROGRESS","BLOCKED","IDLE","DONE","WAITING"].includes(x)) return x;
  return x || "—";
}

function renderList(id, items, empty = "—", max = 8) {
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
  arr.slice(0, max).forEach(x => {
    const li = document.createElement("li");
    li.textContent = clampStr(x);
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
    li.textContent = "No active tasks.";
    ul.appendChild(li);
    return;
  }
  arr.slice(0, 8).forEach(t => {
    const li = document.createElement("li");
    li.textContent = `[${statusNorm(t.status)}] ${t.role ? t.role + ": " : ""}${t.text || ""}`;
    ul.appendChild(li);
  });
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
    tdWork.textContent = clampStr(row.working_on || "", 90);
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

function renderGitHub(recent) {
  const ul = document.getElementById("githubList");
  if (!ul) return;
  ul.innerHTML = "";

  const arr = recent || [];
  if (!arr.length) {
    const li = document.createElement("li");
    li.textContent = "No commits.";
    ul.appendChild(li);
    return;
  }

  arr.slice(0, 8).forEach(c => {
    const li = document.createElement("li");
    li.textContent = `${c.when || ""}  ${c.hash || ""}  ${c.subject || ""}`.trim();
    ul.appendChild(li);
  });
}

function renderConsole(lines) {
  const el = document.getElementById("consoleText");
  if (!el) return;

  const base = (lines || []).slice(0, 18);
  const pulse = `[PULSE] ${new Date().toLocaleTimeString()} heartbeat`;
  el.textContent = [...base, pulse].join("\n");
}

function nodeStyle(status) {
  const s = statusNorm(status);
  if (s === "BLOCKED") return { dash: "10 7", pulse: 0.2 };
  if (s === "IN_PROGRESS") return { dash: "3 3", pulse: 1.0 };
  if (s === "ACTIVE") return { dash: "0", pulse: 0.6 };
  if (s === "DONE") return { dash: "0", pulse: 0.35 };
  if (s === "WAITING") return { dash: "2 8", pulse: 0.25 };
  return { dash: "0", pulse: 0.15 };
}

function drawEdge(parent, x1, y1, x2, y2, status) {
  const p = document.createElementNS("http://www.w3.org/2000/svg", "path");
  const midx = (x1 + x2) / 2;
  const midy = (y1 + y2) / 2;
  const dx = (x2 - x1) * 0.14;
  const dy = (y2 - y1) * 0.14;
  p.setAttribute("d", `M ${x1} ${y1} Q ${midx + dy} ${midy - dx} ${x2} ${y2}`);
  p.setAttribute("stroke", "#111");
  p.setAttribute("stroke-width", "2");
  p.setAttribute("fill", "none");

  const s = statusNorm(status);
  if (s === "BLOCKED") p.setAttribute("stroke-dasharray", "12 9");
  else if (s === "IN_PROGRESS") p.setAttribute("stroke-dasharray", "4 4");
  else p.setAttribute("stroke-dasharray", "2 10");

  parent.appendChild(p);
  return p;
}

function drawNode(parent, x, y, w, h, label, status, subline = "") {
  const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
  const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");

  rect.setAttribute("x", x - w / 2);
  rect.setAttribute("y", y - h / 2);
  rect.setAttribute("rx", "10");
  rect.setAttribute("ry", "10");
  rect.setAttribute("width", w);
  rect.setAttribute("height", h);
  rect.setAttribute("stroke", "#111");
  rect.setAttribute("stroke-width", "2");
  rect.setAttribute("fill", "#fff");

  const st = nodeStyle(status);
  if (st.dash && st.dash !== "0") rect.setAttribute("stroke-dasharray", st.dash);

  text.setAttribute("x", x);
  text.setAttribute("y", y - 2);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("font-size", "13");
  text.setAttribute("fill", "#111");
  text.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  text.textContent = clampStr(label, 22);

  sub.setAttribute("x", x);
  sub.setAttribute("y", y + 16);
  sub.setAttribute("text-anchor", "middle");
  sub.setAttribute("font-size", "11");
  sub.setAttribute("fill", "#111");
  sub.setAttribute("opacity", "0.7");
  sub.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  sub.textContent = clampStr(subline, 30);

  g.appendChild(rect);
  g.appendChild(text);
  if (subline) g.appendChild(sub);
  parent.appendChild(g);

  return { group: g, pulse: st.pulse };
}

let _anim = { started: false, edges: [], nodes: [], t: 0 };

function renderDiagram(snapshot) {
  const edgesEl = document.getElementById("edges");
  const nodesEl = document.getElementById("nodes");
  if (!edgesEl || !nodesEl) return;

  edgesEl.innerHTML = "";
  nodesEl.innerHTML = "";

  const team = snapshot.team || [];
  const products = snapshot.products || [];

  const cx = 550, cy = 300;

  _anim.edges = [];
  _anim.nodes = [];

  _anim.nodes.push(drawNode(nodesEl, cx, cy, 220, 64, "MOXIE", "ACTIVE", "autonomous CMO"));

  const roles = team
    .filter(r => String(r.role || "").toLowerCase() !== "moxie")
    .slice(0, 12);

  const radius = 230;
  const start = -Math.PI / 2;
  const step = roles.length ? (2 * Math.PI) / roles.length : 0;

  roles.forEach((r, i) => {
    const a = start + i * step;
    const x = cx + Math.cos(a) * radius;
    const y = cy + Math.sin(a) * radius;
    _anim.edges.push(drawEdge(edgesEl, cx, cy, x, y, r.status));
    _anim.nodes.push(drawNode(nodesEl, x, y, 230, 60, String(r.role || "ROLE"), r.status, r.working_on || ""));
  });

  // products at bottom
  const py = 570;
  const startX = 360;
  const gap = 190;
  products.slice(0, 4).forEach((p, i) => {
    const x = startX + i * gap;
    _anim.edges.push(drawEdge(edgesEl, cx, cy + 12, x, py, "ACTIVE"));
    _anim.nodes.push(drawNode(nodesEl, x, py, 170, 50, String(p.name || "PRODUCT"), p.status || "ACTIVE", "product"));
  });

  startAnimation();
}

function startAnimation() {
  if (_anim.started) return;
  _anim.started = true;

  const sweep = document.getElementById("sweepRect");

  function frame() {
    _anim.t += 1;

    // sweep left->right
    if (sweep) {
      const x = (-550 + (_anim.t * 2.2) % 1650);
      sweep.setAttribute("x", String(x));
    }

    // edges: animate dash offset
    _anim.edges.forEach((p, idx) => {
      const dash = p.getAttribute("stroke-dasharray") || "";
      const fast = dash === "4 4" ? 2.2 : (dash === "12 9" ? 0.4 : 1.0);
      p.style.strokeDashoffset = String((_anim.t * fast + idx * 7) % 400);
    });

    // node pulse (scale)
    _anim.nodes.forEach((n, idx) => {
      const g = n.group;
      const pulse = n.pulse || 0.2;
      const s = 1 + Math.sin((_anim.t / 18) + idx) * 0.015 * pulse;
      g.setAttribute("transform", `translate(0 0) scale(${s})`);
    });

    requestAnimationFrame(frame);
  }

  requestAnimationFrame(frame);
}

function applySnapshot(snap) {
  setText("generatedAt", `Snapshot: ${fmtDate(snap.generated_at || "")}`);

  setText("kpiPv", snap.kpis?.pageviews_7d ?? "—");
  setText("kpiVisitors", snap.kpis?.visitors_7d ?? "—");
  setText("kpiSignups", snap.kpis?.signups_7d ?? "—");
  setText("kpiPaid", snap.kpis?.paid_7d ?? "—");
  setText("kpiMrr", snap.kpis?.mrr_usd ?? 0);
  setText("kpiRevenueTotal", snap.kpis?.revenue_total_usd ?? 0);

  const active = (snap.products || []).find(p => statusNorm(p.status) === "ACTIVE") || (snap.products || [])[0];
  setText("activeProduct", active ? active.name : "—");

  const q = snap.systems?.queue;
  setText("queueState", q ? `${q.in_progress} in progress • ${q.pending} pending` : "—");

  const runningCount = snap.running?.count ?? (snap.running?.tasks || []).length;
  setText("runningCount", runningCount ?? "—");

  setText("blockerCount", snap.systems?.blockers?.count ?? "—");
  setText("cronCount", snap.systems?.cron?.active_jobs ?? "—");

  renderOpsTasks(snap.running?.tasks || []);
  renderList("highlights", snap.running?.highlights || [], "—");
  renderList("blockersList", snap.systems?.blockers?.needs_rishi || [], "—");

  renderTeam(snap.team || []);
  renderProducts(snap.products || []);
  renderGitHub(snap.github?.recent || []);
  renderConsole(snap.console || []);

  const ticker = document.getElementById("ticker");
  if (ticker) {
    const parts = [];
    parts.push(`running=${runningCount}`);
    parts.push(`blockers=${snap.systems?.blockers?.count ?? 0}`);
    parts.push(`queue_in_progress=${q?.in_progress ?? 0}`);
    parts.push(`pv_7d=${snap.kpis?.pageviews_7d ?? 0}`);
    ticker.textContent = parts.join("  •  ");
  }

  renderDiagram(snap);
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
      console: [...SAMPLE.console, `[FALLBACK] snapshot unavailable (${e.message})`]
    });
  }
}

load();
