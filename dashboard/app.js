/*
  Moxie HQ (public) — SCADA / terminal aesthetic.
  Requirements:
  - modern responsive layout inside one retro window (7.css)
  - draggable nodes in the network map
  - nodes should not overlap by default, and collision-avoid when dragged
  - DO NOT show product nodes in the org chart
*/

const SAMPLE = {
  generated_at: "2026-04-01T00:00:00Z",
  kpis: {
    pageviews_7d: 103,
    visitors_7d: 76,
    signups_7d: 4,
    paid_lifetime: 0,
    free_lifetime: 0,
    revenue_lifetime_usd: 0,
    mrr_usd: 0
  },
  products: [
    { name: "FormBeep", status: "ACTIVE", pageviews_7d: 103, signups_7d: 4 }
  ],
  systems: {
    queue: { pending: 0, in_progress: 0 },
    cron: { active_jobs: 0 },
    blockers: { count: 0, needs_rishi: [] }
  },
  running: {
    count: 0,
    tasks: [],
    highlights: []
  },
  team: [
    { name: "Moxie", title: "Autonomous CMO", status: "ACTIVE", working_on: "Orchestration + decisions" }
  ],
  github: { recent: [] },
  console: [
    "[BOOT] Moxie HQ online",
    "[SYNC] snapshot loaded"
  ]
};

function setText(id, value) {
  const el = document.getElementById(id);
  if (el) el.textContent = value;
}

function fmtDate(iso) {
  try { return new Date(iso).toLocaleString(); } catch { return iso; }
}

function clampStr(s, n = 110) {
  const t = String(s || "");
  return t.length > n ? t.slice(0, n - 1) + "…" : t;
}

function statusNorm(s) {
  const x = String(s || "").toUpperCase();
  if (["ACTIVE","IN_PROGRESS","BLOCKED","IDLE","DONE","WAITING","COMPLETED","QUEUED"].includes(x)) return x;
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
    const badge = document.createElement("span");
    badge.className = "badge";
    badge.textContent = statusNorm(t.status);
    const text = document.createElement("span");
    text.textContent = `${t.role ? t.role + ": " : ""}${t.text || ""}`;
    li.appendChild(badge);
    li.appendChild(text);
    ul.appendChild(li);
  });
}

function renderTeam(team) {
  const tbody = document.getElementById("teamRows");
  if (!tbody) return;
  tbody.innerHTML = "";

  (team || []).forEach(row => {
    const tr = document.createElement("tr");
    const tdEmp = document.createElement("td");
    const tdStatus = document.createElement("td");
    const tdWork = document.createElement("td");

    const name = row.name || "";
    const title = row.title ? ` — ${row.title}` : "";
    tdEmp.textContent = `${name}${title}`;

    tdStatus.textContent = statusNorm(row.status);
    tdWork.textContent = clampStr(row.working_on || "", 90);

    tr.appendChild(tdEmp);
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

// ---- SVG / SCADA MAP (draggable nodes + non-overlap) ----

function clientToSvg(svg, clientX, clientY) {
  const pt = svg.createSVGPoint();
  pt.x = clientX;
  pt.y = clientY;
  const ctm = svg.getScreenCTM();
  if (!ctm) return { x: 0, y: 0 };
  const inv = ctm.inverse();
  const p = pt.matrixTransform(inv);
  return { x: p.x, y: p.y };
}

function nodePulse(status) {
  const s = statusNorm(status);
  if (s === "IN_PROGRESS") return 1.0;
  if (s === "ACTIVE") return 0.6;
  if (s === "BLOCKED") return 0.15;
  if (s === "WAITING" || s === "QUEUED") return 0.22;
  return 0.25;
}

function nodeDash(status) {
  const s = statusNorm(status);
  if (s === "BLOCKED") return "10 7";
  if (s === "IN_PROGRESS") return "3 3";
  if (s === "WAITING" || s === "QUEUED") return "2 8";
  return "0";
}

function edgeDash(status) {
  const s = statusNorm(status);
  if (s === "BLOCKED") return "12 9";
  if (s === "IN_PROGRESS") return "4 4";
  return "2 10";
}

let SCADA = {
  started: false,
  t: 0,
  svg: null,
  edgesEl: null,
  nodesEl: null,
  edges: [], // {path, a, b, dash}
  nodes: [], // {outer, inner, x, y, w, h, pulse, dragHandle}
  dragging: null
};

function drawEdge(aIdx, bIdx, status) {
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  path.setAttribute("stroke", "#111");
  path.setAttribute("stroke-width", "2");
  path.setAttribute("fill", "none");
  const dash = edgeDash(status);
  path.setAttribute("stroke-dasharray", dash);
  SCADA.edgesEl.appendChild(path);
  return { path, a: aIdx, b: bIdx, dash };
}

function drawNode(x, y, w, h, label, status, subline) {
  const outer = document.createElementNS("http://www.w3.org/2000/svg", "g");
  outer.setAttribute("transform", `translate(${x} ${y})`);

  const inner = document.createElementNS("http://www.w3.org/2000/svg", "g");

  const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  rect.setAttribute("x", -w / 2);
  rect.setAttribute("y", -h / 2);
  rect.setAttribute("rx", "10");
  rect.setAttribute("ry", "10");
  rect.setAttribute("width", w);
  rect.setAttribute("height", h);
  rect.setAttribute("stroke", "#111");
  rect.setAttribute("stroke-width", "2");
  rect.setAttribute("fill", "#fff");

  const dash = nodeDash(status);
  if (dash !== "0") rect.setAttribute("stroke-dasharray", dash);

  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", 0);
  text.setAttribute("y", -3);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("font-size", "14");
  text.setAttribute("fill", "#111");
  text.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  text.textContent = clampStr(label, 18);

  const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
  sub.setAttribute("x", 0);
  sub.setAttribute("y", 18);
  sub.setAttribute("text-anchor", "middle");
  sub.setAttribute("font-size", "11");
  sub.setAttribute("fill", "#111");
  sub.setAttribute("opacity", "0.72");
  sub.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  sub.textContent = clampStr(subline || "", 26);

  inner.appendChild(rect);
  inner.appendChild(text);
  if (subline) inner.appendChild(sub);
  outer.appendChild(inner);
  SCADA.nodesEl.appendChild(outer);

  return {
    outer,
    inner,
    x,
    y,
    w,
    h,
    pulse: nodePulse(status),
    dragHandle: rect
  };
}

function updateEdges() {
  for (const e of SCADA.edges) {
    const A = SCADA.nodes[e.a];
    const B = SCADA.nodes[e.b];
    if (!A || !B) continue;
    const x1 = A.x, y1 = A.y;
    const x2 = B.x, y2 = B.y;
    const midx = (x1 + x2) / 2;
    const midy = (y1 + y2) / 2;
    const dx = (x2 - x1) * 0.14;
    const dy = (y2 - y1) * 0.14;
    e.path.setAttribute("d", `M ${x1} ${y1} Q ${midx + dy} ${midy - dx} ${x2} ${y2}`);
  }
}

function setNodePos(idx, x, y) {
  const n = SCADA.nodes[idx];
  if (!n) return;
  n.x = x;
  n.y = y;
  n.outer.setAttribute("transform", `translate(${x} ${y})`);
}

function resolveCollisions(movedIdx = null) {
  // Simple repulsion so nodes don't sit on top of each other.
  const pad = 18;
  const iter = 8;

  for (let k = 0; k < iter; k++) {
    for (let i = 0; i < SCADA.nodes.length; i++) {
      if (movedIdx !== null && i !== movedIdx) continue;
      const A = SCADA.nodes[i];
      if (!A) continue;

      for (let j = 0; j < SCADA.nodes.length; j++) {
        if (i === j) continue;
        const B = SCADA.nodes[j];
        if (!B) continue;

        const ax = A.x, ay = A.y;
        const bx = B.x, by = B.y;

        const dx = ax - bx;
        const dy = ay - by;
        const dist = Math.sqrt(dx * dx + dy * dy) || 0.0001;

        // approximate node radius
        const ra = Math.max(A.w, A.h) * 0.55;
        const rb = Math.max(B.w, B.h) * 0.55;
        const minDist = ra + rb + pad;

        if (dist < minDist) {
          const push = (minDist - dist) * 0.55;
          const ux = dx / dist;
          const uy = dy / dist;

          // move A away
          setNodePos(i, ax + ux * push, ay + uy * push);
        }
      }
    }
  }
}

function clampToViewbox(idx) {
  const n = SCADA.nodes[idx];
  if (!n) return;
  const vbW = 1100, vbH = 700;
  const marginX = n.w / 2 + 20;
  const marginY = n.h / 2 + 20;
  const x = Math.min(vbW - marginX, Math.max(marginX, n.x));
  const y = Math.min(vbH - marginY, Math.max(marginY, n.y));
  setNodePos(idx, x, y);
}

function attachDrag(idx) {
  const n = SCADA.nodes[idx];
  if (!n || !SCADA.svg) return;
  const svg = SCADA.svg;

  n.dragHandle.style.cursor = "grab";

  n.dragHandle.addEventListener("pointerdown", (ev) => {
    ev.preventDefault();
    n.dragHandle.setPointerCapture(ev.pointerId);
    const p = clientToSvg(svg, ev.clientX, ev.clientY);
    SCADA.dragging = {
      idx,
      offsetX: n.x - p.x,
      offsetY: n.y - p.y
    };
    n.dragHandle.style.cursor = "grabbing";
  });

  n.dragHandle.addEventListener("pointermove", (ev) => {
    if (!SCADA.dragging || SCADA.dragging.idx !== idx) return;
    const p = clientToSvg(svg, ev.clientX, ev.clientY);
    setNodePos(idx, p.x + SCADA.dragging.offsetX, p.y + SCADA.dragging.offsetY);
    clampToViewbox(idx);
    resolveCollisions(idx);
    updateEdges();
  });

  const end = () => {
    if (!SCADA.dragging || SCADA.dragging.idx !== idx) return;
    SCADA.dragging = null;
    n.dragHandle.style.cursor = "grab";
    resolveCollisions(null);
    updateEdges();
  };

  n.dragHandle.addEventListener("pointerup", end);
  n.dragHandle.addEventListener("pointercancel", end);
};

function startAnimation() {
  if (SCADA.started) return;
  SCADA.started = true;

  const sweep = document.getElementById("sweepRect");

  function frame() {
    SCADA.t += 1;

    // sweep left->right
    if (sweep) {
      const x = (-550 + (SCADA.t * 2.4) % 1650);
      sweep.setAttribute("x", String(x));
    }

    // animate edges
    SCADA.edges.forEach((e, idx) => {
      const dash = e.dash;
      const fast = dash === "4 4" ? 2.2 : (dash === "12 9" ? 0.5 : 1.1);
      e.path.style.strokeDashoffset = String((SCADA.t * fast + idx * 7) % 400);
    });

    // node inner pulse (doesn't affect position)
    SCADA.nodes.forEach((n, idx) => {
      const p = n.pulse;
      const s = 1 + Math.sin((SCADA.t / 18) + idx) * 0.02 * p;
      n.inner.setAttribute("transform", `scale(${s})`);
    });

    requestAnimationFrame(frame);
  }

  requestAnimationFrame(frame);
}

function renderDiagram(snapshot) {
  SCADA.svg = document.getElementById("orgSvg");
  SCADA.edgesEl = document.getElementById("edges");
  SCADA.nodesEl = document.getElementById("nodes");
  if (!SCADA.svg || !SCADA.edgesEl || !SCADA.nodesEl) return;

  SCADA.edgesEl.innerHTML = "";
  SCADA.nodesEl.innerHTML = "";
  SCADA.edges = [];
  SCADA.nodes = [];

  const team = snapshot.team || [];

  const cx = 550, cy = 330;

  // center
  const mox = drawNode(cx, cy, 240, 70, "MOXIE", "ACTIVE", "autonomous CMO");
  SCADA.nodes.push(mox);

  // ring (stable spacing, no touching)
  const roles = team
    .filter(r => String((r.name || "")).toLowerCase() !== "moxie")
    .slice(0, 12);

  const radius = 245;
  const start = -Math.PI / 2;
  const step = roles.length ? (2 * Math.PI) / roles.length : 0;

  roles.forEach((r, i) => {
    const a = start + i * step;
    const x = cx + Math.cos(a) * radius;
    const y = cy + Math.sin(a) * radius;

    const label = String(r.name || "ROLE");
    const subtitle = String(r.title || "");

    const node = drawNode(x, y, 240, 64, label, r.status, subtitle);
    const idx = SCADA.nodes.push(node) - 1;

    // edge to center
    SCADA.edges.push(drawEdge(0, idx, r.status));
  });

  // avoid any collisions on initial render
  resolveCollisions(null);
  for (let i = 0; i < SCADA.nodes.length; i++) clampToViewbox(i);

  // attach drag
  for (let i = 0; i < SCADA.nodes.length; i++) attachDrag(i);

  updateEdges();
  startAnimation();
}

function applySnapshot(snap) {
  setText("generatedAt", `Snapshot: ${fmtDate(snap.generated_at || "")}`);

  setText("kpiPv", snap.kpis?.pageviews_7d ?? "—");
  setText("kpiVisitors", snap.kpis?.visitors_7d ?? "—");
  setText("kpiSignups", snap.kpis?.signups_7d ?? "—");

  setText("kpiPaidLifetime", snap.kpis?.paid_lifetime ?? 0);
  setText("kpiFreeLifetime", snap.kpis?.free_lifetime ?? 0);
  setText("kpiRevenueLifetime", snap.kpis?.revenue_lifetime_usd ?? 0);
  setText("kpiMrr", snap.kpis?.mrr_usd ?? 0);

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
