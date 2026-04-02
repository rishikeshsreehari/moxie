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
    users_lifetime: "—",
    paid_lifetime: 0,
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
  const raw = String(s || "").trim();
  const x = raw.toUpperCase();
  if (!x) return "—";

  // canonicalize common variants
  if (x.includes("BLOCK")) return "BLOCKED";
  if (x.includes("IN_PROGRESS") || x.includes("IN PROGRESS") || x.includes("WIP")) return "IN_PROGRESS";
  if (x.includes("WAIT")) return "WAITING";
  if (x.includes("QUEUE")) return "QUEUED";
  if (x.includes("ACTIVE")) return "ACTIVE";
  if (x.includes("DONE") || x.includes("COMPLETE")) return "COMPLETED";
  if (x.includes("IDLE")) return "IDLE";

  // last resort
  if (["ACTIVE","IN_PROGRESS","BLOCKED","IDLE","DONE","WAITING","COMPLETED","QUEUED"].includes(x)) return x;
  return x;
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

function dotClass(status) {
  const s = statusNorm(status);
  if (s === "ACTIVE") return "active";
  if (s === "IN_PROGRESS") return "in_progress";
  if (s === "BLOCKED") return "blocked";
  if (s === "IDLE" || s === "COMPLETED" || s === "DONE" || s === "WAITING" || s === "QUEUED") return "idle";
  return "idle";
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
      tdStatus.innerHTML = `<span class="status-dot ${dotClass(status)}"></span><span class="badge">${status}</span>`;
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
      right.innerHTML = `<span class="status-dot ${dotClass(status)}"></span><span class="badge">${status}</span>`;

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

function money(v) {
  if (v === null || v === undefined || v === "") return "—";
  const n = Number(v);
  if (Number.isNaN(n)) return String(v);
  return n.toFixed(n % 1 === 0 ? 0 : 2);
}

function renderProducts(products) {
  const tbody = document.getElementById("productRows");
  if (tbody) tbody.innerHTML = "";

  const cards = document.getElementById("productCards");
  if (cards) cards.innerHTML = "";

  (products || []).forEach(p => {
    const status = statusNorm(p.status);
    const customers = String(p.paid_lifetime ?? p.users_lifetime ?? "—");
    const life = money(p.revenue_lifetime_usd);
    const mrr = money(p.mrr_usd);

    const nameEl = (function () {
      const a = document.createElement("a");
      a.textContent = p.name;
      if (p.url) {
        a.href = p.url;
        a.target = "_blank";
        a.rel = "noopener";
      } else {
        a.href = "#";
      }
      return a;
    })();

    if (tbody) {
      const tr = document.createElement("tr");
      const tdName = document.createElement("td");
      const tdStatus = document.createElement("td");
      const tdUsers = document.createElement("td");
      const tdLife = document.createElement("td");
      const tdMrr = document.createElement("td");

      tdName.appendChild(nameEl);
      tdStatus.innerHTML = `<span class="status-dot ${dotClass(status)}"></span><span class="badge">${status}</span>`;
      tdUsers.textContent = customers;
      tdLife.textContent = life;
      tdMrr.textContent = mrr;

      tr.appendChild(tdName);
      tr.appendChild(tdStatus);
      tr.appendChild(tdUsers);
      tr.appendChild(tdLife);
      tr.appendChild(tdMrr);
      tbody.appendChild(tr);
    }

    if (cards) {
      const wrap = document.createElement("div");
      wrap.className = "cardrow";

      const top = document.createElement("div");
      top.className = "rowtop";

      const left = document.createElement("div");
      left.className = "rowname";
      left.appendChild(nameEl.cloneNode(true));

      const right = document.createElement("div");
      right.className = "mono";
      right.innerHTML = `<span class="status-dot ${dotClass(status)}"></span><span class="badge">${status}</span>`;

      top.appendChild(left);
      top.appendChild(right);

      const meta = document.createElement("div");
      meta.className = "rowmeta";
      meta.textContent = `Customers: ${customers} • Lifetime: $${life} • MRR: $${mrr}`;

      wrap.appendChild(top);
      wrap.appendChild(meta);
      cards.appendChild(wrap);
    }
  });
}

function renderShipLog(recent) {
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

  arr.slice(0, 10).forEach(c => {
    const li = document.createElement("li");
    const prefix = `${c.when || ""}  ${c.repo ? "[" + c.repo + "]" : ""}  ${c.hash || ""}`.trim();

    if (c.url) {
      const a = document.createElement("a");
      a.href = c.url;
      a.target = "_blank";
      a.rel = "noopener";
      a.textContent = `${prefix}  ${c.subject || ""}`.trim();
      li.appendChild(a);
    } else {
      li.textContent = `${prefix}  ${c.subject || ""}`.trim();
    }

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

function renderModelBars(models) {
  const el = document.getElementById("modelBars");
  if (!el) return;

  const items = (models && models.items) ? models.items : [];
  if (!items.length) {
    el.textContent = "(no model data)";
    return;
  }

  const max = Math.max(...items.map(x => Number(x.value || 0)));
  el.innerHTML = "";

  items.slice(0, 6).forEach(x => {
    const row = document.createElement("div");
    row.className = "modelbar";

    const label = document.createElement("div");
    label.textContent = `${x.label} (${x.value})`;

    const bar = document.createElement("div");
    bar.className = "bar";

    const fill = document.createElement("span");
    const pct = max ? Math.round((Number(x.value || 0) / max) * 100) : 0;
    fill.style.width = `${pct}%`;

    bar.appendChild(fill);
    row.appendChild(label);
    row.appendChild(bar);
    el.appendChild(row);
  });
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
  const podsEl = document.getElementById("pods");
  if (!SCADA.svg || !SCADA.edgesEl || !SCADA.nodesEl) return;

  if (podsEl) podsEl.innerHTML = "";
  SCADA.edgesEl.innerHTML = "";
  SCADA.nodesEl.innerHTML = "";
  SCADA.edges = [];
  SCADA.nodes = [];
  SCADA.dragging = null;

  function podOf(t) {
    const title = String(t.title || "").toLowerCase();
    const name = String(t.name || "").toLowerCase();
    const hay = `${name} ${title}`;
    if (hay.includes("engineer") || hay.includes("full stack") || hay.includes("dev")) return "ENGINEERING";
    if (hay.includes("analytics") || hay.includes("report") || hay.includes("data")) return "ANALYTICS";
    if (hay.includes("outreach") || hay.includes("distribution") || hay.includes("directory")) return "DISTRIBUTION";
    if (hay.includes("copy") || hay.includes("conversion")) return "CONVERSION";
    if (hay.includes("competitor") || hay.includes("research") || hay.includes("growth")) return "GROWTH";
    return "GROWTH";
  }

  // Center node: MOXIE
  const cx = 550, cy = 330;
  SCADA.nodes.push(drawNode(cx, cy, 200, 76, "MOXIE", "ACTIVE", "Autonomous ops"));

  // Pod layout (cluster centers)
  const pods = [
    { key: "GROWTH", x: 280, y: 205, w: 460, h: 250 },
    { key: "ENGINEERING", x: 820, y: 205, w: 460, h: 250 },
    { key: "DISTRIBUTION", x: 280, y: 520, w: 460, h: 250 },
    { key: "ANALYTICS", x: 820, y: 520, w: 460, h: 250 },
    { key: "CONVERSION", x: 550, y: 520, w: 460, h: 250 }
  ];

  const people = [];
  (snapshot.team || []).forEach(t => {
    const nm = (t.name || "").trim();
    if (!nm || nm.toLowerCase() === "moxie") return;
    people.push({
      label: nm,
      status: statusNorm(t.status || "IDLE"),
      sub: clampStr(t.title || "", 56),
      pod: podOf(t)
    });
  });

  const usedPods = new Set(people.map(p => p.pod));

  function drawPodBox(el, p) {
    const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

    const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    r.setAttribute("x", String(p.x - p.w / 2));
    r.setAttribute("y", String(p.y - p.h / 2));
    r.setAttribute("width", String(p.w));
    r.setAttribute("height", String(p.h));
    r.setAttribute("rx", "12");
    r.setAttribute("ry", "12");
    r.setAttribute("fill", "rgba(255,255,255,0.55)");
    r.setAttribute("stroke", "#111");
    r.setAttribute("stroke-width", "2");
    r.setAttribute("filter", "url(#noise)");

    const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
    t.setAttribute("x", String(p.x - p.w / 2 + 14));
    t.setAttribute("y", String(p.y - p.h / 2 + 22));
    t.setAttribute("fill", "#111");
    t.setAttribute("font-size", "14");
    t.setAttribute("font-family", "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', monospace");
    t.textContent = p.key;

    g.appendChild(r);
    g.appendChild(t);
    el.appendChild(g);
  }

  if (podsEl) {
    pods.forEach(p => {
      if (usedPods.has(p.key)) drawPodBox(podsEl, p);
    });
  }

  const byPod = {};
  people.forEach(p => {
    byPod[p.pod] = byPod[p.pod] || [];
    byPod[p.pod].push(p);
  });

  const podLookup = {};
  pods.forEach(p => { podLookup[p.key] = p; });

  let idx = 1;
  Object.keys(byPod).forEach(pk => {
    const box = podLookup[pk] || { x: cx, y: cy, w: 460, h: 250 };
    const arr = byPod[pk] || [];
    const r = Math.max(64, Math.min(140, 45 + arr.length * 10));

    arr.slice(0, 10).forEach((n, i) => {
      const ang = (Math.PI * 2) * (i / Math.max(1, arr.length));
      const x = box.x + Math.cos(ang) * r;
      const y = box.y + Math.sin(ang) * (r * 0.70);
      SCADA.nodes.push(drawNode(x, y, 220, 72, n.label || "", n.status, n.sub));
      SCADA.edges.push(drawEdge(0, idx, n.status));
      idx += 1;
    });
  });

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
  const prods = (snapshot.products || []).map(p => p.name).filter(Boolean);
  if (prods.length) lines.push(`Products: ${prods.join(" + ")}`);
  lines.push(`Traffic 7D: ${k.pageviews_7d ?? 0} pv / ${k.visitors_7d ?? 0} visitors`);
  lines.push(`Signups 7D: ${k.signups_7d ?? 0} • Customers lifetime: ${k.paid_lifetime ?? "—"}`);
  lines.push(`Revenue lifetime: $${k.revenue_lifetime_usd ?? 0} • MRR: $${k.mrr_usd ?? 0}`);
  lines.push(`Queue: ${(snapshot.systems?.queue?.in_progress ?? 0)} in progress, ${(snapshot.systems?.queue?.pending ?? 0)} pending`);
  const insight = (snapshot.insights || [])[Math.floor(Math.random() * Math.max(1, (snapshot.insights || []).length))];
  if (insight) lines.push(`Insight: ${insight}`);
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
  // KPI tile: "CUSTOMERS (LIFETIME)" is paid customers
  setText("kpiUsersLifetime", String(k.paid_lifetime ?? "—"));
  setText("kpiRevenueLifetime", String(k.revenue_lifetime_usd ?? "—"));
  setText("kpiMrr", String(k.mrr_usd ?? "—"));

  // Product links (optional override from snapshot)
  const prodLinks = document.getElementById("productLinks");
  if (prodLinks && Array.isArray(snapshot.products) && snapshot.products.length) {
    const links = snapshot.products
      .filter(p => p && p.url)
      .slice(0, 4)
      .map(p => `<a href="${p.url}" target="_blank" rel="noopener">${p.link_label || p.url.replace(/^https?:\/\//, "")}</a>`)
      .join(" • ");
    if (links) prodLinks.innerHTML = `Products: ${links}`;
  }

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
  renderShipLog((snapshot.shipping?.recent || snapshot.github?.recent || []));
  renderModelBars(snapshot.models || {});
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
// test
