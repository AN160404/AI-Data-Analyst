import sys
from pathlib import Path

_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

import streamlit as st
from utils.api_client import health
from utils.config import get_api_base
from utils.theme import apply_theme

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon=":material/dashboard:",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

# ── Inject custom CSS ────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ── Root palette (Power BI-inspired) ─────────────────────── */
    :root {
        --navy:        #0B1D3A;
        --navy-mid:    #112244;
        --navy-light:  #1A3360;
        --gold:        #F2C811;
        --gold-dim:    #D4AE0F;
        --gold-pale:   #FDF3C0;
        --slate:       #8A9BB5;
        --white:       #F5F7FA;
        --card-bg:     #111D35;
        --card-border: rgba(242,200,17,0.18);
        --text-primary:#E8EDF5;
        --text-muted:  #8A9BB5;
        --accent-teal: #00B4C6;
        --accent-rose: #E8406A;
        --accent-green:#21C97A;
        --accent-purple:#7B61FF;
        --radius:      14px;
        --radius-lg:   22px;
    }

    /* ── Global reset ─────────────────────────────────────────── */
    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], .main {
        color: var(--text-primary) !important;
        font-family: 'Figtree', sans-serif !important;
    }

    /* Gradient background + subtle white mesh */
    [data-testid="stAppViewContainer"] {
        background:
            linear-gradient(rgba(255,255,255,0.028) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.028) 1px, transparent 1px),
            radial-gradient(ellipse 70% 55% at 8% 0%, rgba(242,200,17,0.09) 0%, transparent 70%),
            radial-gradient(ellipse 60% 50% at 95% 100%, rgba(0,180,198,0.07) 0%, transparent 65%),
            linear-gradient(160deg, #0D2248 0%, #0B1D3A 45%, #091628 100%) !important;
        background-size:
            40px 40px,
            40px 40px,
            100% 100%,
            100% 100%,
            100% 100% !important;
        background-attachment: fixed !important;
    }

    /* Keep inner containers transparent so the bg shows through */
    .block-container, .main, [data-testid="stMain"] {
        background: transparent !important;
    }

    [data-testid="stSidebar"] {
        background: var(--navy-mid) !important;
        border-right: 1px solid rgba(242,200,17,0.12) !important;
    }

    /* Push content well below Streamlit's sticky header bar (~3.5rem tall) */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 1400px;
    }

    /* ── Banner strip ─────────────────────────────────────────── */
    .banner-strip {
        background: linear-gradient(90deg, var(--navy-light) 0%, #0D2A55 100%);
        border: 1px solid var(--card-border);
        border-radius: var(--radius);
        padding: 10px 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        margin-top: 0.5rem;
        margin-bottom: 2.2rem;
    }
    .banner-dot {
        width: 9px; height: 9px;
        border-radius: 50%;
        background: var(--gold);
        box-shadow: 0 0 8px var(--gold);
        flex-shrink: 0;
        animation: pulse 2.2s ease-in-out infinite;
    }
    @keyframes pulse {
        0%,100% { opacity:1; transform:scale(1); }
        50%      { opacity:.55; transform:scale(1.35); }
    }
    .banner-text { font-size: 0.82rem; color: var(--slate); letter-spacing: .04em; }
    .banner-badge {
        margin-left: auto;
        background: rgba(242,200,17,0.13);
        border: 1px solid rgba(242,200,17,0.3);
        color: var(--gold);
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 600;
        padding: 3px 12px;
        letter-spacing: .06em;
        text-transform: uppercase;
    }

    /* ── Hero ─────────────────────────────────────────────────── */
    .hero-eyebrow {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: .14em;
        text-transform: uppercase;
        color: var(--gold);
        margin-bottom: 10px;
    }
    .hero-title {
        font-size: clamp(2.4rem, 4.5vw, 3.6rem);
        font-weight: 800;
        line-height: 1.08;
        color: var(--white);
        margin: 0 0 18px 0;
        letter-spacing: -0.02em;
    }
    .hero-title span {
        background: linear-gradient(135deg, var(--gold) 30%, #FFE77A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        line-height: 1.7;
        color: var(--slate);
        max-width: 560px;
        margin-bottom: 10px;
    }
    .hero-cta-row {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 28px;
    }
    .cta-primary {
        background: var(--gold);
        color: var(--navy);
        font-weight: 700;
        font-size: 0.9rem;
        padding: 12px 28px;
        border-radius: 8px;
        letter-spacing: .04em;
        text-decoration: none;
        display: inline-block;
    }
    .cta-secondary {
        background: transparent;
        border: 1px solid rgba(242,200,17,0.35);
        color: var(--gold);
        font-weight: 600;
        font-size: 0.9rem;
        padding: 12px 28px;
        border-radius: 8px;
        letter-spacing: .04em;
        text-decoration: none;
        display: inline-block;
    }

    /* ── Status card ──────────────────────────────────────────── */
    .status-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: var(--radius-lg);
        padding: 28px 26px;
        height: 100%;
    }
    .status-label {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .1em;
        color: var(--slate);
        margin-bottom: 16px;
    }
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: .05em;
        margin-bottom: 14px;
    }
    .status-pill.connected {
        background: rgba(33,201,122,0.12);
        border: 1px solid rgba(33,201,122,0.35);
        color: var(--accent-green);
    }
    .status-pill.disconnected {
        background: rgba(232,64,106,0.12);
        border: 1px solid rgba(232,64,106,0.35);
        color: var(--accent-rose);
    }
    .status-pill-dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: currentColor;
    }
    .status-url {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        color: var(--text-muted);
        background: rgba(255,255,255,0.04);
        border-radius: 6px;
        padding: 8px 12px;
        word-break: break-all;
        line-height: 1.5;
    }
    .status-metric {
        display: flex;
        flex-direction: column;
        margin-top: 18px;
        padding-top: 18px;
        border-top: 1px solid rgba(255,255,255,0.06);
    }
    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: var(--gold);
        letter-spacing: -0.02em;
        line-height: 1;
    }
    .metric-label {
        font-size: 0.72rem;
        color: var(--text-muted);
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    /* ── Section divider ──────────────────────────────────────── */
    .section-divider {
        display: flex;
        align-items: center;
        gap: 16px;
        margin: 2.8rem 0 2rem 0;
    }
    .section-divider-line {
        flex: 1;
        height: 1px;
        background: rgba(255,255,255,0.07);
    }
    .section-divider-label {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .14em;
        color: var(--slate);
        white-space: nowrap;
    }

    /* ── Feature cards ────────────────────────────────────────── */
    .feature-card {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: var(--radius-lg);
        padding: 26px 22px;
        height: 100%;
        position: relative;
        overflow: hidden;
        transition: border-color .25s, transform .25s;
    }
    .feature-card:hover {
        border-color: rgba(242,200,17,0.25);
        transform: translateY(-3px);
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: var(--radius-lg) var(--radius-lg) 0 0;
    }
    .feature-card.ac1::before { background: var(--gold); }
    .feature-card.ac2::before { background: var(--accent-teal); }
    .feature-card.ac3::before { background: var(--accent-green); }
    .feature-card.ac4::before { background: var(--accent-purple); }

    .feature-icon {
        font-size: 1.7rem;
        margin-bottom: 14px;
        display: block;
    }
    .feature-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 8px;
    }
    .feature-desc {
        font-size: 0.84rem;
        line-height: 1.6;
        color: var(--text-muted);
        margin: 0;
    }
    .feature-tag {
        display: inline-block;
        margin-top: 14px;
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .08em;
        padding: 3px 10px;
        border-radius: 20px;
    }
    .feature-card.ac1 .feature-tag { background: rgba(242,200,17,0.12); color: var(--gold); }
    .feature-card.ac2 .feature-tag { background: rgba(0,180,198,0.12); color: var(--accent-teal); }
    .feature-card.ac3 .feature-tag { background: rgba(33,201,122,0.12); color: var(--accent-green); }
    .feature-card.ac4 .feature-tag { background: rgba(123,97,255,0.12); color: var(--accent-purple); }

    /* ── Nav links section ────────────────────────────────────── */
    .nav-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
        gap: 12px;
        margin-top: 0;
    }
    .nav-item {
        background: var(--card-bg);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: var(--radius);
        padding: 16px 18px;
        display: flex;
        align-items: flex-start;
        gap: 12px;
        transition: border-color .2s, background .2s;
    }
    .nav-item:hover {
        border-color: rgba(242,200,17,0.3);
        background: rgba(242,200,17,0.04);
    }
    .nav-item-icon {
        font-size: 1.15rem;
        flex-shrink: 0;
        margin-top: 1px;
    }
    .nav-item-body {}
    .nav-item-title {
        font-size: 0.87rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 3px;
    }
    .nav-item-desc {
        font-size: 0.78rem;
        color: var(--text-muted);
        line-height: 1.45;
        margin: 0;
    }

    /* ── Stat strip ───────────────────────────────────────────── */
    .stat-strip {
        background: linear-gradient(90deg, var(--navy-light) 0%, #0D274E 100%);
        border: 1px solid var(--card-border);
        border-radius: var(--radius-lg);
        padding: 22px 30px;
        display: flex;
        gap: 0;
        align-items: center;
        margin: 2.2rem 0 0 0;
    }
    .stat-item {
        flex: 1;
        text-align: center;
        position: relative;
    }
    .stat-item + .stat-item::before {
        content: '';
        position: absolute;
        left: 0; top: 10%; bottom: 10%;
        width: 1px;
        background: rgba(255,255,255,0.08);
    }
    .stat-num {
        font-size: 1.65rem;
        font-weight: 800;
        color: var(--gold);
        letter-spacing: -0.02em;
    }
    .stat-lbl {
        font-size: 0.72rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: .09em;
        margin-top: 3px;
    }

    /* ── Streamlit overrides ──────────────────────────────────── */
    .stMarkdown p { color: var(--text-primary) !important; }
    hr { border-color: rgba(255,255,255,0.06) !important; }
    [data-testid="column"] { gap: 0 !important; }

    /* Blend Streamlit's sticky header bar into the navy theme */
    [data-testid="stHeader"] {
        background: var(--navy) !important;
        border-bottom: 1px solid rgba(242,200,17,0.08) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── API health check ──────────────────────────────────────────────────────────
ok, body = health()

# ── Banner strip ──────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="banner-strip">
        <div class="banner-dot"></div>
        <span class="banner-text">Enterprise analytics experience &nbsp;·&nbsp; Intelligent data workflows &nbsp;·&nbsp; AI-driven decisions</span>
        <span class="banner-badge">Premium Analytics</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Hero + Status ─────────────────────────────────────────────────────────────
col1, col2 = st.columns([2.4, 1], gap="large")

with col1:
    st.markdown(
        """
        <div class="hero-eyebrow">Intelligent Analytics Platform</div>
        <h1 class="hero-title">AI <span>Data Analyst</span></h1>
        <p class="hero-subtitle">
            A polished analytics workspace for modern businesses. Upload data, validate
            workflows, generate actionable insights, forecast outcomes, and interact with
            a powerful AI agent — all in one professional platform.
        </p>
        <p class="hero-subtitle">
            Designed for teams that need fast business intelligence without sacrificing
            clarity, trust, or presentation quality.
        </p>
        <div class="hero-cta-row">
            <span class="cta-primary">📤 Upload Dataset</span>
            <span class="cta-secondary">🤖 Open AI Analyst</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    if ok:
        status_label = "Connected"
        pill_class = "connected"
        url_text = get_api_base()
    else:
        status_label = "Disconnected"
        pill_class = "disconnected"
        url_text = f"{get_api_base()} — Start with: uvicorn backend.main:app --reload"

    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">Backend Status</div>
            <div class="status-pill {pill_class}">
                <div class="status-pill-dot"></div>
                {status_label}
            </div>
            <div class="status-url">{url_text}</div>
            <div class="status-metric">
                <div class="metric-value">4</div>
                <div class="metric-label">Active modules</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not ok and isinstance(body, dict) and body.get("error"):
        st.caption(body["error"])

# ── Stats strip ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="stat-strip">
        <div class="stat-item">
            <div class="stat-num">CSV&nbsp;·&nbsp;XLSX</div>
            <div class="stat-lbl">Supported formats</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">Real-time</div>
            <div class="stat-lbl">AI inference</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">SQL + NL</div>
            <div class="stat-lbl">Query modes</div>
        </div>
        <div class="stat-item">
            <div class="stat-num">∞</div>
            <div class="stat-lbl">Chart types</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Feature cards ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Platform Capabilities</div>
        <div class="section-divider-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

features = [
    ("ac1", "📤", "Dataset Onboarding",      "Ingest",   "Capture and validate CSV/XLSX data with a modern intake workflow including schema inference and cleaning summaries."),
    ("ac2", "💡", "Insight Suite",            "Analyze",  "Generate KPI dashboards, narrative summaries, and forecasts from your registered datasets in seconds."),
    ("ac3", "📊", "Workflow Intelligence",    "Inspect",  "Review pipeline transformations, dependency chains, and SQL execution flow with full lineage tracking."),
    ("ac4", "🤖", "AI Analyst",              "Collaborate","Collaborate with the agent to answer business questions, create charts, and refine data-driven decisions."),
]

f_cols = st.columns(4, gap="small")
for col, (ac, icon, title, tag, desc) in zip(f_cols, features):
    col.markdown(
        f"""
        <div class="feature-card {ac}">
            <span class="feature-icon">{icon}</span>
            <div class="feature-title">{title}</div>
            <p class="feature-desc">{desc}</p>
            <span class="feature-tag">{tag}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Quick navigation ──────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="section-divider">
        <div class="section-divider-line"></div>
        <div class="section-divider-label">Quick Navigation</div>
        <div class="section-divider-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

nav_items = [
    ("📤", "Dataset Onboarding",     "Register CSV/XLSX and review cleaning summary, schema, and preview."),
    ("🗂️", "Registered Datasets",    "View registered dataset names, metadata, and column profiles."),
    ("💡", "Insights Suite",          "Produce business insights, KPIs, and visual summaries instantly."),
    ("📊", "Workflow Intelligence",   "Inspect the SQL pipeline and end-to-end data flow diagram."),
    ("🤖", "AI Analyst",             "Interact with the AI agent and visualize chart recommendations."),
]

nav_html = '<div class="nav-grid">'
for icon, title, desc in nav_items:
    nav_html += f"""
    <div class="nav-item">
        <div class="nav-item-icon">{icon}</div>
        <div class="nav-item-body">
            <div class="nav-item-title">{title}</div>
            <p class="nav-item-desc">{desc}</p>
        </div>
    </div>"""
nav_html += "</div>"

st.markdown(nav_html, unsafe_allow_html=True)