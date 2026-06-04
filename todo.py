import streamlit as st
import json
import os
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="✦ TASKS",
    page_icon="✦",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Space+Mono:wght@400;700&display=swap');

:root {
    --bg: #0a0a0f;
    --surface: #12121a;
    --border: #2a2a3a;
    --accent: #c8ff00;
    --accent2: #ff6b6b;
    --text: #e8e8f0;
    --muted: #5a5a7a;
}

html, body, [class*="css"] {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem !important; max-width: 700px !important; }

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 3rem 0 2rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 5rem;
    font-weight: 800;
    letter-spacing: -4px;
    color: var(--accent);
    line-height: 1;
    margin: 0;
    text-shadow: 0 0 60px rgba(200,255,0,0.3);
}
.hero-sub {
    font-size: 0.75rem;
    color: var(--muted);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-top: 0.5rem;
}
.hero-date {
    font-size: 0.7rem;
    color: var(--muted);
    margin-top: 0.25rem;
}

/* ── Stats row ── */
.stats-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
}
.stat-box {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 1rem;
    text-align: center;
    clip-path: polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 10px 100%, 0 calc(100% - 10px));
}
.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--accent);
    line-height: 1;
}
.stat-label {
    font-size: 0.6rem;
    color: var(--muted);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 0.25rem;
}

/* ── Input area ── */
.stTextInput input {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-left: 3px solid var(--accent) !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.9rem !important;
    padding: 0.75rem 1rem !important;
    border-radius: 0 !important;
}
.stTextInput input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 20px rgba(200,255,0,0.1) !important;
}

/* ── Buttons ── */
.stButton button {
    background: var(--accent) !important;
    color: #000 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 0.6rem 1.5rem !important;
    cursor: pointer !important;
    transition: all 0.15s !important;
    clip-path: polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 8px 100%, 0 calc(100% - 8px)) !important;
}
.stButton button:hover {
    background: #d4ff1a !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(200,255,0,0.3) !important;
}

/* ── Task items ── */
.task-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 1.25rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid transparent;
    margin-bottom: 0.5rem;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
}
.task-item::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: var(--accent);
    transform: scaleY(0);
    transition: transform 0.2s;
}
.task-item:hover::before { transform: scaleY(1); }
.task-item.done {
    opacity: 0.45;
    border-left-color: var(--muted);
}
.task-item.done::before { background: var(--muted); }
.task-tag {
    display: inline-block;
    font-size: 0.6rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 2px 8px;
    border: 1px solid;
    margin-left: 0.5rem;
}
.tag-high { color: var(--accent2); border-color: var(--accent2); }
.tag-med  { color: #ffcc44; border-color: #ffcc44; }
.tag-low  { color: var(--muted); border-color: var(--muted); }

/* ── Section header ── */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--muted);
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.5rem;
    margin: 1.5rem 0 1rem;
}

/* ── Progress bar ── */
.progress-wrap {
    height: 4px;
    background: var(--border);
    margin-bottom: 1.5rem;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), #44ffaa);
    transition: width 0.4s ease;
}

/* ── Select boxes ── */
.stSelectbox div[data-baseweb="select"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 0 !important;
    color: var(--text) !important;
}

/* ── Checkbox ── */
.stCheckbox label { font-family: 'Space Mono', monospace !important; font-size: 0.85rem !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--accent); }
</style>
""", unsafe_allow_html=True)

# ── State ────────────────────────────────────────────────────────────────────
SAVE_FILE = "/tmp/fancy_tasks.json"

def load_tasks():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return []

def save_tasks(tasks):
    with open(SAVE_FILE, "w") as f:
        json.dump(tasks, f)

if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

tasks = st.session_state.tasks

# ── Hero ──────────────────────────────────────────────────────────────────────
now = datetime.now()
st.markdown(f"""
<div class="hero">
  <p class="hero-title">TASKS</p>
  <p class="hero-sub">✦ Command Center ✦</p>
  <p class="hero-date">{now.strftime('%A, %B %d  ·  %H:%M')}</p>
</div>
""", unsafe_allow_html=True)

# ── Stats ─────────────────────────────────────────────────────────────────────
total = len(tasks)
done_count = sum(1 for t in tasks if t.get("done"))
pending = total - done_count
pct = int(done_count / total * 100) if total else 0

st.markdown(f"""
<div class="stats-row">
  <div class="stat-box"><div class="stat-num">{total}</div><div class="stat-label">Total</div></div>
  <div class="stat-box"><div class="stat-num">{pending}</div><div class="stat-label">Pending</div></div>
  <div class="stat-box"><div class="stat-num">{done_count}</div><div class="stat-label">Done</div></div>
  <div class="stat-box"><div class="stat-num">{pct}%</div><div class="stat-label">Complete</div></div>
</div>
<div class="progress-wrap"><div class="progress-fill" style="width:{pct}%"></div></div>
""", unsafe_allow_html=True)

# ── Add task ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">// Add New Task</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([5, 2, 2])
with col1:
    new_task = st.text_input("", placeholder="What needs to be done?", label_visibility="collapsed")
with col2:
    priority = st.selectbox("", ["High", "Medium", "Low"], label_visibility="collapsed")
with col3:
    add_clicked = st.button("+ ADD", use_container_width=True)

if add_clicked and new_task.strip():
    tasks.append({
        "text": new_task.strip(),
        "done": False,
        "priority": priority,
        "created": now.strftime("%b %d, %H:%M"),
        "id": int(datetime.now().timestamp() * 1000),
    })
    save_tasks(tasks)
    st.rerun()

# ── Filter ────────────────────────────────────────────────────────────────────
col_f1, col_f2 = st.columns([3, 2])
with col_f1:
    st.markdown('<div class="section-header">// Task List</div>', unsafe_allow_html=True)
with col_f2:
    filter_mode = st.selectbox("", ["All", "Pending", "Done"], label_visibility="collapsed", key="filter")

filtered = [t for t in tasks if (
    filter_mode == "All" or
    (filter_mode == "Pending" and not t.get("done")) or
    (filter_mode == "Done" and t.get("done"))
)]

# ── Render tasks ──────────────────────────────────────────────────────────────
if not filtered:
    st.markdown("""
    <div style="text-align:center;padding:3rem;color:#5a5a7a;font-size:0.8rem;letter-spacing:2px;text-transform:uppercase;">
        ✦ No tasks here ✦
    </div>
    """, unsafe_allow_html=True)

delete_ids = []
toggle_ids = []

for i, task in enumerate(filtered):
    prio = task.get("priority", "Medium")
    tag_class = "tag-high" if prio == "High" else ("tag-med" if prio == "Medium" else "tag-low")
    done_class = "done" if task.get("done") else ""
    strike = "text-decoration:line-through;" if task.get("done") else ""

    st.markdown(f"""
    <div class="task-item {done_class}">
      <div style="flex:1">
        <span style="{strike}color:var(--text);font-size:0.9rem;">{task['text']}</span>
        <span class="task-tag {tag_class}">{prio}</span>
        <div style="font-size:0.65rem;color:var(--muted);margin-top:0.35rem;letter-spacing:1px;">
          ◎ Added {task.get('created','—')}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, _ = st.columns([2, 2, 6])
    with c1:
        label = "↩ UNDO" if task.get("done") else "✓ DONE"
        if st.button(label, key=f"tog_{task['id']}_{i}", use_container_width=True):
            toggle_ids.append(task["id"])
    with c2:
        if st.button("✕ DEL", key=f"del_{task['id']}_{i}", use_container_width=True):
            delete_ids.append(task["id"])

# ── Apply mutations ───────────────────────────────────────────────────────────
changed = False
for tid in toggle_ids:
    for t in tasks:
        if t["id"] == tid:
            t["done"] = not t["done"]
            changed = True
for tid in delete_ids:
    tasks[:] = [t for t in tasks if t["id"] != tid]
    changed = True

if changed:
    save_tasks(tasks)
    st.rerun()

# ── Clear all done ────────────────────────────────────────────────────────────
if done_count:
    st.markdown('<div class="section-header">// Bulk Actions</div>', unsafe_allow_html=True)
    if st.button(f"✕ CLEAR {done_count} COMPLETED TASK{'S' if done_count>1 else ''}", use_container_width=True):
        st.session_state.tasks = [t for t in tasks if not t.get("done")]
        save_tasks(st.session_state.tasks)
        st.rerun()