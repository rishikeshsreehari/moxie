/*
  SapiensTech Open Ops (public) — 7.css monochrome.
  - modern responsive layout inside one retro window
  - draggable nodes in the network map
  - collision-avoid when dragged
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
    "[BOOT] Open Ops online",
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
  if (tbody) tbody.innerHTML = "";

  const cards = document.getElementById("teamCards");
  if (cards) cards.innerHTML = "";

  (team || []).forEach(row => {
    const name = row.name || "";
    const title = row.title ? ` — ${row.title}` : "";
    const status = statusNorm(row.status);
    const working = clampStr(row.working_on || "", 160);

    if (tbody) {
      const tr = document.createElement("tr");
      const tdEmp = document.createElement("td");
      const tdStatus = document.createElement("td");
      const tdWork = document.createElement("td");

      tdEmp.textContent = `${name}${title}`;
      tdStatus.textContent = status;
      tdWork.textContent = clampStr(row.working_on || "", 90);

      tr.appendChild(tdEmp);
      tr.appendChild(tdStatus);
      tr.appendChild(tdWork);
      tbody.appendChild(tr);
    }

    if (cards) {
      const wrap = document.createElement("div");
      wrap.className = "cardrow";

      const top = document.createElement("div");
      top.className = "rowtop";

      const left = document.createElement("div");
      left.className = "rowname";
      left.textContent = `${name}${title}`;

      const right = document.createElement("div");
      right.className = "mono";
      right.innerHTML = `<span class="badge">${status}</span>`;

      top.appendChild(left);
      top.appendChild(right);

      const meta = document.createElement("div");
      meta.className = "rowmeta";
      meta.textContent = working || "—";

      wrap.appendChild(top);
      wrap.appendChild(meta);
      cards.appendChild(wrap);
    }
  });
}

function renderProducts(products) {
  const tbody = document.getElementById("productRows");
  if (tbody) tbody.innerHTML = "";

  const cards = document.getElementById("productCards");
  if (cards) cards.innerHTML = "";

  (products || []).forEach(p => {
    const status = statusNorm(p.status);
    const pv = String(p.pageviews_7d ?? "—");
    const su = String(p.signups_7d ?? "—");

    if (tbody) {
      const tr = document.createElement("tr");
      const tdName = document.createElement("td");
      const tdStatus = document.createElement("td");
      const tdPv = document.createElement("td");
      const tdSignups = document.createElement("td");

      tdName.textContent = p.name;
      tdStatus.textContent = status;
      tdPv.textContent = pv;
      tdSignups.textContent = su;

      tr.appendChild(tdName);
      tr.appendChild(tdStatus);
      tr.appendChild(tdPv);
      tr.appendChild(tdSignups);
      tbody.appendChild(tr);
    }

    if (cards) {
      const wrap = document.createElement("div");
      wrap.className = "cardrow";

      const top = document.createElement("div");
      top.className = "rowtop";

      const left = document.createElement("div");
      left.className = "rowname";
      left.textContent = p.name;

      const right = document.createElement("div");
      right.className = "mono";
      right.innerHTML = `<span class="badge">${status}</span>`;

      top.appendChild(left);
      top.appendChild(right);

      const meta = document.createElement("div");
      meta.className = "rowmeta";
      meta.textContent = `7D PV: ${pv} • 7D Signups: ${su}`;

      wrap.appendChild(top);
      wrap.appendChild(meta);
      cards.appendChild(wrap);
    }
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

function renderTerminal(lines) {
  const el = document.getElementById("terminalText");
  if (!el) return;
  const arr = (lines || []).slice(0, 60);
  el.textContent = arr.length ? arr.join("\n") : "$ echo 'no data'\nno data";
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
  edges: [],
  nodes: [],
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
  text.setAttribute("x", "0");
  text.setAttribute("y", -3);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("font-size", "14");
  text.setAttribute("fill", "#111");
  text.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace");
  text.textContent = clampStr(label, 18);

  const sub = document.createElementNS("http://www.w3.org/2000/svg", "text");
  sub.setAttribute("x", "0");
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

  return { outer, inner, dragHandle: rect, x, y, w, h, pulse: nodePulse(status) };
}

function setNodePos(idx, x, y) {
  const n = SCADA.nodes[idx];
  if (!n) return;
  n.x = x;
  n.y = y;
  n.outer.setAttribute("transform", `translate(${x} ${y})`);
}

function updateEdges() {
  SCADA.edges.forEach(e => {
    const A = SCADA.nodes[e.a];
    const B = SCADA.nodes[e.b];
    if (!A || !B) return;

    const ax = A.x, ay = A.y;
    const bx = B.x, by = B.y;

    const mx = (ax + bx) / 2;
    const my = (ay + by) / 2;

    const d = `M ${ax} ${ay} Q ${mx} ${my} ${bx} ${by}`;
    e.path.setAttribute("d", d);
  });
}

function resolveCollisions(activeIdx = null) {
  const pad = 12;
  for (let iter = 0; iter < 2; iter++) {
    for (let i = 0; i < SCADA.nodes.length; i++) {
      if (activeIdx !== null && i !== activeIdx) continue;
      const A = SCADA.nodes[i];
      if (!A) continue;

      for (let j = 0; j < SCADA.nodes.length; j++) {
        if (i === j) continue;
        const B = SCADA.nodes[j];
        if (!B) continue;

        const dx = A.x - B.x;
        const dy = A.y - B.y;
        const dist = Math.sqrt(dx * dx + dy * dy) || 0.0001;

        const ra = Math.max(A.w, A.h) * 0.55;
        const rb = Math.max(B.w, B.h) * 0.55;
        const minDist = ra + rb + pad;

        if (dist < minDist) {
          const push = (minDist - dist) * 0.55;
          const ux = dx / dist;
          const uy = dy / dist;
          setNodePos(i, A.x + ux * push, A.y + uy * push);
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
}

function startAnimation() {
  if (SCADA.started) return;
  SCADA.started = true;

  const sweep = document.getElementById("sweepRect");

  function frame() {
    SCADA.t += 1;

    if (sweep) {
      const x = (-550 + (SCADA.t * 2.4) % 1650);
      sweep.setAttribute("x", String(x));
    }

    SCADA.edges.forEach((e, idx) => {
      const dash = e.dash;
      const fast = dash === "4 4" ? 2.2 : (dash === "12 9" ? 0.5 : 1.1);
      e.path.style.strokeDashoffset = String((SCADA.t * fast + idx * 7) % 400);
    });

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
  SCADA.dragging = null;

  // Center node: MOXIE
  const nodes = [];
  nodes.push({ label: "MOXIE", status: "ACTIVE", sub: "Autonomous ops" });

  // Team nodes only (no product nodes)
  (snapshot.team || []).forEach(t => {
    nodes.push({
      label: t.name || "",
      status: t.status || "IDLE",
      sub: t.title || ""
    });
  });

  // Layout
  const cx = 550, cy = 330;
  const ring = 240;

  // MOXIE
  SCADA.nodes.push(drawNode(cx, cy, 200, 76, nodes[0].label, nodes[0].status, nodes[0].sub));

  // Team around
  const teamCount = Math.max(0, nodes.length - 1);
  for (let i = 0; i < teamCount; i++) {
    const angle = (Math.PI * 2) * (i / Math.max(1, teamCount));
    const x = cx + Math.cos(angle) * ring;
    const y = cy + Math.sin(angle) * (ring * 0.78);
    const n = nodes[i + 1];
    SCADA.nodes.push(drawNode(x, y, 220, 72, n.label || "", n.status, n.sub));
  }

  // Edges from MOXIE to each team node
  for (let i = 1; i < SCADA.nodes.length; i++) {
    const st = nodes[i]?.status || "ACTIVE";
    SCADA.edges.push(drawEdge(0, i, st));
  }

  // Non-overlap settle
  resolveCollisions(null);
  for (let i = 0; i < SCADA.nodes.length; i++) clampToViewbox(i);
  updateEdges();

  // Drag
  for (let i = 0; i < SCADA.nodes.length; i++) attachDrag(i);

  startAnimation();
}

function pickTicker(snapshot) {
  const lines = [];
  const k = snapshot.kpis || {};
  const active = (snapshot.products || []).find(p => String(p.status || "").toUpperCase() === "ACTIVE");
  if (active) lines.push(`Focus: ${active.name}`);
  lines.push(`Traffic 7D: ${k.pageviews_7d ?? 0} pv / ${k.visitors_7d ?? 0} visitors`);
  lines.push(`Signups 7D: ${k.signups_7d ?? 0} • Paid lifetime: ${k.paid_lifetime ?? 0}`);
  lines.push(`Revenue lifetime: $${k.revenue_lifetime_usd ?? 0} • MRR: $${k.mrr_usd ?? 0}`);
  lines.push(`Queue: ${(snapshot.systems?.queue?.in_progress ?? 0)} in progress, ${(snapshot.systems?.queue?.pending ?? 0)} pending`);
  return lines[Math.floor(Math.random() * lines.length)];
}

async function loadSnapshot() {
  try {
    const res = await fetch("./public_snapshot.json", { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (e) {
    return SAMPLE;
  }
}

function renderAll(snapshot) {
  const k = snapshot.kpis || {};

  setText("generatedAt", `snapshot: ${fmtDate(snapshot.generated_at || "")}`);

  setText("kpiPv", String(k.pageviews_7d ?? "—"));
  setText("kpiVisitors", String(k.visitors_7d ?? "—"));
  setText("kpiSignups", String(k.signups_7d ?? "—"));
  setText("kpiPaidLifetime", String(k.paid_lifetime ?? "—"));
  setText("kpiFreeLifetime", String(k.free_lifetime ?? "—"));
  setText("kpiRevenueLifetime", String(k.revenue_lifetime_usd ?? "—"));
  setText("kpiMrr", String(k.mrr_usd ?? "—"));

  // Active product
  const active = (snapshot.products || []).find(p => String(p.status || "").toUpperCase() === "ACTIVE");
  setText("activeProduct", active ? active.name : "—");

  // Systems
  setText("runningCount", String(snapshot.running?.count ?? 0));
  setText("queueState", `${snapshot.systems?.queue?.in_progress ?? 0} in_progress • ${snapshot.systems?.queue?.pending ?? 0} pending`);
  setText("blockerCount", String(snapshot.systems?.blockers?.count ?? 0));
  setText("cronCount", String(snapshot.systems?.cron?.active_jobs ?? 0));

  renderOpsTasks(snapshot.running?.tasks || []);
  renderList("highlights", snapshot.running?.highlights || [], "—", 8);
  renderList("blockersList", snapshot.systems?.blockers?.needs_rishi || [], "—", 8);
  renderTeam(snapshot.team || []);
  renderProducts(snapshot.products || []);
  renderGitHub(snapshot.github?.recent || []);
  renderConsole(snapshot.console || []);
  renderTerminal(snapshot.terminal_lines || []);

  renderDiagram(snapshot);

  const tick = () => {
    const el = document.getElementById("ticker");
    if (el) el.textContent = pickTicker(snapshot);
  };
  tick();
  setInterval(tick, 3200);
}

function startClock() {
  const el = document.getElementById("liveClock");
  if (!el) return;
  const step = () => {
    el.textContent = new Date().toLocaleString();
  };
  step();
  setInterval(step, 1000);
}

(async function init() {
  startClock();
  const snapshot = await loadSnapshot();
  renderAll(snapshot);
})();
