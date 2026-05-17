import streamlit as st


def apply_theme():
    """Apply the unified dark theme to Streamlit app."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

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

        html, body {
            background: transparent !important;
            color: var(--text-primary) !important;
            font-family: 'Figtree', sans-serif !important;
        }

        [data-testid="stAppViewContainer"] {
            background:
                repeating-linear-gradient(
                    0deg,
                    rgba(255,255,255,0.028) 0px,
                    rgba(255,255,255,0.028) 1px,
                    transparent 1px,
                    transparent 40px
                ),
                repeating-linear-gradient(
                    90deg,
                    rgba(255,255,255,0.028) 0px,
                    rgba(255,255,255,0.028) 1px,
                    transparent 1px,
                    transparent 40px
                ),
                radial-gradient(circle at top left, rgba(242,200,17,0.09), transparent 24%),
                radial-gradient(circle at bottom right, rgba(0,180,198,0.07), transparent 28%),
                linear-gradient(160deg, #0D2248 0%, #0B1D3A 50%, #091628 100%);
            background-attachment: fixed;
        }

        [data-testid="stMain"], .main, .block-container {
            background: transparent !important;
        }

        [data-testid="stSidebar"] {
            background: var(--navy-mid) !important;
            border-right: 1px solid rgba(242,200,17,0.12) !important;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        header {
            background: var(--navy) !important;
            border-bottom: 1px solid rgba(242,200,17,0.15) !important;
        }

        .block-container { padding-top: 3rem !important; padding-bottom: 3rem !important; }

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

        .stMarkdown p { color: var(--text-primary) !important; }
        hr { border-color: rgba(255,255,255,0.06) !important; }
        [data-testid="column"] { gap: 0 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
