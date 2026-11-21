"""
Swetha Rani Keshava Ravi — Analytics Portfolio (Streamlit)

Run locally:
    pip install -r requirements.txt
    streamlit run app.py

Optional files in the same folder:
    CV-Swetha.pdf          -> enables the "Download CV" buttons
    profile.jpg / .png     -> replaces the initials placeholder with your photo
"""

from pathlib import Path
from html import escape
from urllib.parse import urlparse

import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Swetha Rani | Analytics Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
RESUME_PATH = BASE_DIR / "CV-Swetha.pdf"


# =========================================================
# PERSONAL DETAILS — EDIT YOUR LINKS HERE
# =========================================================
PROFILE = {
    "name": "Swetha Rani Keshava Ravi",
    "short_name": "Swetha Rani",
    "initials": "SR",
    "title": "Business Analytics & Financial Data",
    "location": "Vermillion, South Dakota",
    "email": "swetharanikr10@gmail.com",
    "phone": "+1 605-736-6973",
    "linkedin": "https://www.linkedin.com/in/swetha-rani-keshava-ravi-6a92071ab/",
    "github": "https://github.com/swetharanikr10",
}

SUMMARY = (
    "Business Analytics graduate student with 4+ years of experience in financial "
    "data operations and quantitative analysis. Skilled in Python, SQL, R, time series "
    "forecasting, statistical analysis, and predictive modeling, with hands-on projects "
    "in financial risk assessment and market data analysis. Experienced in communicating "
    "data-driven findings to portfolio managers, financial advisers, and institutional "
    "clients. Strong interest in quantitative finance, risk analytics, and data-driven "
    "decision-making."
)

PROJECT_LINKS = {
    "spy": "https://github.com/swetharanikr10/Predicting-Future-Returns",
    "nlp": "https://github.com/swetharanikr10/Risk-Language-Across-Industries",
    "risk": "https://github.com/swetharanikr10/Financial-Risk-Analysis-and-Predictive-Modeling-Using-Machine-Learning",
    "bitcoin": "https://github.com/swetharanikr10/Time-Series-Forecast-Model-of-Bitcoin-Prices",
    "gold": "https://github.com/swetharanikr10/swetharanikr10-Gold-Price-Analysis-and-Forecasting-Using-Time-Series-Techniques-2016-2026-",
    "yield_curve": "https://github.com/swetharanikr10/Dynamic-Yield-Curve-Modelling-using-the-Nelson-Siegel-Yield-Only-Framework-1990-2026-",
    "options": "https://github.com/swetharanikr10/Options-Fundamentals",
}


# =========================================================
# HTML RENDERER (fixes raw HTML showing as code blocks)
# =========================================================
def md(body, **_):
    """Render HTML safely: strip indentation and blank lines so Markdown
    never mistakes indented HTML for a code block."""
    flat = "\n".join(line.strip() for line in str(body).splitlines() if line.strip())
    st.markdown(flat, unsafe_allow_html=True)


# =========================================================
# LIGHT PASTEL SAGE / PALE TEAL THEME
# (base layout + your colour overrides)
# =========================================================
md(
    """
    <style>
        :root {
            --background: #FAFBF8;
            --surface: #FFFFFF;
            --surface-alt: #EDF5EF;
            --border: #D5E3D9;
            --forest: #354D46;
            --green: #45675D;
            --bronze: #AECDBD;
            --text: #35443F;
            --muted: #586B63;
        }

        .stApp { background: #FAFBF8; color: #35443F; }
        header[data-testid="stHeader"] { background: #FAFBF8; }
        .block-container { max-width: 1180px; padding-top: 5.5rem; }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: #E3F0E7 !important;
            border-right: 1px solid #C9DDD0 !important;
        }
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] a,
        [data-testid="stSidebar"] span { color: #354D46 !important; }
        [data-testid="stSidebar"] svg { color: #354D46 !important; }
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: #CEE3D6 !important;
            border-left: 3px solid #789F8C !important;
            border-radius: 8px;
        }
        [data-testid="stSidebarNav"] a:hover { background: #D7E9DD !important; }

        .sidebar-monogram {
            width: 56px; height: 56px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 20px; letter-spacing: .04em;
            background: #C8E0D8 !important; color: #354D46 !important;
            margin-bottom: 10px;
        }
        .sidebar-name { font-weight: 700; font-size: 17px; color: #354D46 !important; }
        .sidebar-subtitle { font-size: 14px; color: #52685E !important; margin-bottom: 6px; }

        /* Headings and text */
        h1, h2, h3, h4 { color: #354D46 !important; letter-spacing: -0.01em; }
        h4 { font-size: 15px !important; margin: 14px 0 4px 0 !important; }
        .eyebrow {
            color: #526E61 !important; font-size: 13px; font-weight: 600;
            letter-spacing: .04em; margin-bottom: 6px;
        }
        .hero-role, .organization { color: #45675D !important; font-weight: 600; }
        .hero-role { font-size: 20px; margin-bottom: 12px; }
        .hero h1 { font-size: clamp(34px, 4.6vw, 50px); line-height: 1.08; margin: 4px 0 8px 0; }
        .hero p, .hero-location, .page-heading p, .meta { color: #586B63 !important; }
        .hero p { font-size: 17px; max-width: 62ch; }
        .hero-location { font-size: 14px; margin: 8px 0 14px 0; }
        .hero-rule { width: 64px; height: 4px; border-radius: 2px; background: #AECDBD !important; margin: 4px 0 10px 0; }
        .meta { font-size: 14px; margin: 2px 0 10px 0; }

        .page-heading { border-bottom: 1px solid #D5E3D9; padding-bottom: 14px; margin-bottom: 22px; }
        .page-heading h1 { margin: 0 0 6px 0; }
        .page-heading p { margin: 0; font-size: 16px; }

        /* Cards */
        .card {
            background: #FFFFFF !important;
            border: 1px solid #D5E3D9 !important;
            border-radius: 12px;
            padding: 20px 22px;
            margin-bottom: 18px;
            box-shadow: 0 5px 18px rgba(75, 105, 88, 0.04);
        }
        .card h3 { margin: 0 0 6px 0; font-size: 19px; line-height: 1.3; }
        .card p, .card li { color: #586B63; }
        .card ul { margin: 6px 0 0 0; padding-left: 20px; }
        .card li { margin: 4px 0; }
        .accent-card { border-top: 3px solid #AECDBD !important; }
        .featured-card { border-left: 4px solid #789F8C !important; }

        .detail-row {
            display: grid; grid-template-columns: 90px minmax(0, 1fr); gap: 12px;
            padding: 10px 0; border-bottom: 1px solid #D5E3D9;
        }
        .detail-row:last-child { border-bottom: 0; }
        .detail-label { color: #586B63 !important; font-size: 14px; }
        .detail-value { color: #354D46 !important; font-weight: 600; overflow-wrap: anywhere; }
        .detail-value a { overflow-wrap: normal; word-break: normal; }

        /* Tags */
        .tag {
            display: inline-block; font-size: 13px; padding: 3px 10px; margin: 4px 6px 0 0;
            border-radius: 999px; border: 1px solid #D5E5DA !important;
            background: #EDF5EF !important; color: #405D50 !important; white-space: nowrap;
        }

        /* Stats */
        .stat {
            background: #FFFFFF !important; border: 1px solid #D5E3D9 !important;
            border-bottom: 3px solid #AECDBD !important; border-radius: 12px;
            padding: 16px 18px; margin-bottom: 18px; height: 100%;
        }
        .stat-value { color: #354D46 !important; font-size: 28px; font-weight: 700; line-height: 1.15; }
        .stat-label { color: #586B63 !important; font-size: 14px; margin-top: 4px; }

        /* Inline result figures inside project cards */
        .results { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin: 12px 0 6px 0; }
        .result { background: #EDF5EF; border-radius: 10px; padding: 10px 12px; }
        .result b { display: block; color: #354D46; font-size: 20px; line-height: 1.2; }
        .result span { color: #586B63; font-size: 13px; }

        .finding {
            background: #F3F8F4; border-left: 3px solid #AECDBD; border-radius: 6px;
            padding: 10px 14px; margin-top: 12px; color: #405D50; font-size: 15px;
        }

        /* Timeline */
        .timeline-item { display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 14px; padding: 10px 0; border-bottom: 1px dashed #D5E3D9; }
        .timeline-item:last-child { border-bottom: 0; }
        .timeline-date { color: #586B63; font-size: 14px; }
        .timeline-role { color: #354D46; font-weight: 600; }
        .timeline-org { color: #586B63; font-size: 14px; }

        .pending, .footer { color: #586B63 !important; }
        .footer { border-top: 1px solid #D5E3D9; margin-top: 36px; padding-top: 16px; font-size: 14px; }

        /* Photo / initials placeholder */
        .profile-placeholder {
            aspect-ratio: 1 / 1; max-width: 320px; margin: 0 auto; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 72px; font-weight: 700; letter-spacing: .04em;
            background: linear-gradient(140deg, #E4F1E8, #D4E9E4) !important;
            border: 3px solid #AECDBD !important; color: #45675D !important;
        }
        [data-testid="stImage"] img { border: 3px solid #AECDBD !important; border-radius: 16px; }

        /* Links and buttons */
        a { color: #45675D; }
        .button-link {
            display: inline-block; text-decoration: none !important; font-weight: 600;
            padding: 8px 16px; margin: 10px 8px 0 0; border-radius: 8px;
            background: #D8EADF !important; border: 1px solid #AECDBD !important; color: #354D46 !important;
        }
        .button-link:hover { background: #C9E0D3 !important; }
        div[data-testid="stButton"] button,
        div[data-testid="stDownloadButton"] button,
        div[data-testid="stLinkButton"] a {
            background: #D8EADF !important; border: 1px solid #AECDBD !important; color: #354D46 !important;
        }
        div[data-testid="stButton"] button p,
        div[data-testid="stDownloadButton"] button p,
        div[data-testid="stLinkButton"] a p { color: #354D46 !important; }
        div[data-testid="stButton"] button:hover,
        div[data-testid="stDownloadButton"] button:hover { background: #C9E0D3 !important; }

        @media (max-width: 640px) {
            .detail-row, .timeline-item { grid-template-columns: minmax(0, 1fr); gap: 2px; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HELPERS
# =========================================================
def text(value):
    return escape(str(value))


def valid_url(value):
    value = (value or "").strip()
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        return escape(value, quote=True)
    return ""


def link_html(url, label):
    url = valid_url(url)
    if not url:
        return ""
    return (
        f'<a class="button-link" href="{url}" target="_blank" rel="noopener noreferrer">'
        f"{text(label)}</a>"
    )


def tags_html(items):
    return "".join(f'<span class="tag">{text(item)}</span>' for item in items)


def bullets_html(items):
    return "<ul>" + "".join(f"<li>{text(item)}</li>" for item in items) + "</ul>"


def results_html(items):
    if not items:
        return ""
    return '<div class="results">' + "".join(
        f'<div class="result"><b>{text(v)}</b><span>{text(l)}</span></div>' for v, l in items
    ) + "</div>"


def heading(title, description=""):
    md(
        f"""
        <div class="page-heading">
            <div class="eyebrow">Swetha Rani / Portfolio</div>
            <h1>{text(title)}</h1>
            <p>{text(description)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card(title, description="", bullets=None, tags=None, extra_class=""):
    content = f"<h3>{text(title)}</h3>"
    if description:
        content += f"<p>{text(description)}</p>"
    if bullets:
        content += bullets_html(bullets)
    if tags:
        content += '<div style="margin-top: 12px;">' + tags_html(tags) + "</div>"
    md(f'<div class="card {extra_class}">{content}</div>', unsafe_allow_html=True)


def stat_row(items):
    columns = st.columns(len(items))
    for column, (value, label) in zip(columns, items):
        with column:
            md(
                f"""
                <div class="stat">
                    <div class="stat-value">{text(value)}</div>
                    <div class="stat-label">{text(label)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def show_photo():
    candidates = ["profile.jpg", "profile.jpeg", "profile.png", "profile.webp"]
    photo_path = next(
        (BASE_DIR / name for name in candidates if (BASE_DIR / name).is_file()),
        None,
    )
    if photo_path:
        st.image(str(photo_path), width="stretch")
    else:
        md(
            f'<div class="profile-placeholder">{text(PROFILE["initials"])}</div>',
            unsafe_allow_html=True,
        )


def resume_button(key):
    if RESUME_PATH.is_file():
        st.download_button(
            label="Download CV",
            data=RESUME_PATH.read_bytes(),
            file_name="Swetha_Rani_CV.pdf",
            mime="application/pdf",
            key=key,
        )


def detail_rows(items):
    return "".join(
        f"""
        <div class="detail-row">
            <div class="detail-label">{text(label)}</div>
            <div class="detail-value">{value}</div>
        </div>
        """
        for label, value in items
    )


# =========================================================
# PROJECTS
# =========================================================
PROJECTS = [
    {
        "key": "spy",
        "featured": True,
        "title": "Predicting Future Returns and Optimizing SPY Options Selection",
        "category": "Derivatives",
        "period": "Graduate project · Operational Analytics",
        "description": (
            "A descriptive, predictive, and prescriptive analytics pipeline in R built on "
            "353,178 SPY option observations."
        ),
        "results": [
            ("353,178", "SPY option observations"),
            ("≈7%", "Lower test RMSE vs. baseline (boosting)"),
            ("5.41%", "Top-decile return vs. −2.41% overall"),
        ],
        "bullets": [
            "Used chronological train/test splits and rolling-origin cross-validation to avoid look-ahead bias.",
            "Compared linear regression, random forest, and gradient boosting; gradient boosting cut test RMSE by about 7% versus the baseline.",
            "Ranked contracts by predicted return: the model's top decile earned 5.41% versus −2.41% across all contracts.",
            "Optimized a daily linear program with lpSolve under capital, liquidity, and concentration limits.",
            "Ran backtesting and sensitivity analysis on the optimized selections.",
        ],
        "finding": (
            "Key finding: backtesting showed the predictive signal did not survive bid-ask "
            "execution costs — an honest test of whether a model edge is tradable."
        ),
        "methods": [
            "Descriptive analysis", "Rolling-origin cross-validation", "Linear regression",
            "Random forest", "Gradient boosting", "Linear programming", "Backtesting",
            "Sensitivity analysis",
        ],
        "tags": ["R", "lpSolve", "Options", "Machine Learning", "Optimization"],
        "link": PROJECT_LINKS["spy"],
    },
    {
        "key": "nlp",
        "featured": True,
        "title": "An NLP-Based Analysis of Risk Disclosures Across Industries (2021–2025)",
        "category": "NLP & Text Analytics",
        "period": "Graduate project · 2021–2025 filings",
        "description": (
            "Extracted Item 1A Risk Factors from 30 SEC Form 10-K filings — 6 companies across "
            "3 industries — and analysed how risk language differs and changes over time."
        ),
        "results": [
            ("30", "Form 10-K filings analysed"),
            ("0.90 vs 0.41", "Within-company vs. within-industry similarity"),
            ("7×+", "Rise in AI-related risk language"),
        ],
        "bullets": [
            "Extracted the Item 1A Risk Factors section from each filing and prepared the text corpus in R.",
            "Applied TF-IDF weighting and cosine similarity to compare disclosures across companies and years.",
            "Used hierarchical clustering and LDA topic modeling to group filings and surface recurring risk themes.",
            "Scored tone with the Loughran-McDonald financial sentiment dictionary.",
        ],
        "finding": (
            "Key findings: filings cluster by company before industry (similarity 0.90 vs. 0.41); "
            "AI-related language rose more than sevenfold while COVID references nearly disappeared."
        ),
        "methods": [
            "TF-IDF", "Cosine similarity", "Hierarchical clustering", "LDA topic modeling",
            "Loughran-McDonald sentiment",
        ],
        "tags": ["R", "NLP", "SEC Filings", "Text Mining", "Risk Disclosures"],
        "link": PROJECT_LINKS["nlp"],
    },
    {
        "key": "risk",
        "featured": False,
        "title": "Financial Risk Assessment Using Statistical Analysis and Machine Learning",
        "category": "Risk Analytics",
        "period": "Independent project",
        "description": (
            "Developed predictive models to assess financial risk using statistical analysis "
            "and machine learning techniques."
        ),
        "results": [],
        "bullets": [
            "Performed exploratory data analysis and feature engineering.",
            "Evaluated model performance to identify key risk drivers and improve prediction accuracy.",
            "Generated actionable insights to support risk management and strategic decision-making.",
        ],
        "finding": "",
        "methods": ["Exploratory data analysis", "Feature engineering", "Predictive modeling", "Model evaluation"],
        "tags": ["Python", "Financial Risk", "Machine Learning", "Statistical Analysis"],
        "link": PROJECT_LINKS["risk"],
    },
    {
        "key": "bitcoin",
        "featured": False,
        "title": "Time Series Forecast Model of Bitcoin Prices",
        "category": "Time Series",
        "period": "Predictive analytics for financial decision-making",
        "description": (
            "Built a time series forecasting model to analyse and predict Bitcoin price "
            "movements using historical market data."
        ),
        "results": [],
        "bullets": [
            "Applied statistical and machine learning techniques to historical market data.",
            "Captured trends, seasonality, and volatility in cryptocurrency markets.",
            "Evaluated model performance to improve forecasting accuracy and support financial decisions.",
        ],
        "finding": "",
        "methods": ["Trend & seasonality analysis", "Volatility analysis", "Forecast evaluation"],
        "tags": ["Bitcoin", "Time Series", "Predictive Analytics", "Market Data"],
        "link": PROJECT_LINKS["bitcoin"],
    },
    {
        "key": "gold",
        "featured": False,
        "title": "Gold Price Analysis and Forecasting Using Time Series Techniques (2016–2026)",
        "category": "Time Series",
        "period": "Independent project · 2016–2026",
        "description": (
            "Analysed 2,510 trading days of historical gold prices to identify trends, "
            "seasonality, and volatility patterns."
        ),
        "results": [
            ("2,510", "Trading days analysed"),
            ("2016–2026", "Study period"),
        ],
        "bullets": [
            "Identified trend, seasonality, and volatility patterns in the price history.",
            "Applied ARIMA and Exponential Smoothing models to forecast gold prices.",
            "Evaluated models with forecasting accuracy metrics and visualised results for investment and economic analysis.",
        ],
        "finding": "",
        "methods": ["ARIMA", "Exponential Smoothing", "Forecast accuracy metrics"],
        "tags": ["Gold", "ARIMA", "Exponential Smoothing", "Forecasting"],
        "link": PROJECT_LINKS["gold"],
    },
    {
        "key": "yield_curve",
        "featured": False,
        "title": "Dynamic Yield Curve Modelling Using the Nelson–Siegel Yield-Only Framework (1990–2026)",
        "category": "Fixed Income",
        "period": "Independent project · 1990–2026",
        "description": (
            "Developed a Nelson–Siegel yield curve model on U.S. Treasury yield data from 1990–2026."
        ),
        "results": [
            ("1990–2026", "U.S. Treasury yield history"),
            ("3", "Factors: level, slope, curvature"),
        ],
        "bullets": [
            "Estimated level, slope, and curvature factors from the Treasury term structure.",
            "Interpreted the factors against macroeconomic and interest rate movements.",
            "Visualised term structure dynamics to support fixed income and monetary policy insights.",
        ],
        "finding": "",
        "methods": ["Nelson–Siegel model", "Factor estimation", "Term structure visualisation"],
        "tags": ["Nelson–Siegel", "Fixed Income", "Treasury Yields", "Term Structure"],
        "link": PROJECT_LINKS["yield_curve"],
    },
    {
        "key": "options",
        "featured": False,
        "title": "Options Fundamentals: Pricing, Moneyness, Implied Volatility & Greeks",
        "category": "Derivatives",
        "period": "Study project",
        "description": (
            "A foundational study of options theory, pricing mechanics, and derivatives risk concepts."
        ),
        "results": [("5", "Greeks covered: Δ, Γ, Θ, ν, ρ")],
        "bullets": [
            "Studied option pricing mechanics, moneyness, and implied volatility.",
            "Examined first- and second-order Greeks: Delta, Gamma, Theta, Vega, and Rho.",
            "Explored the role of Greeks in risk management and hedging.",
            "Built foundational knowledge of market structure to support options analytics.",
        ],
        "finding": "",
        "methods": ["Option pricing", "Moneyness", "Implied volatility", "Greeks", "Hedging"],
        "tags": ["Options", "Greeks", "Implied Volatility", "Hedging"],
        "link": PROJECT_LINKS["options"],
    },
]

PROJECT_CATEGORIES = ["All"] + sorted({p["category"] for p in PROJECTS})


def project_card(number, project, show_methods=True):
    project_link = link_html(project["link"], "View project on GitHub") or (
        '<div class="pending">Repository link to be added</div>'
    )
    finding = f'<div class="finding">{text(project["finding"])}</div>' if project["finding"] else ""
    methods = ""
    if show_methods and project["methods"]:
        methods = "<h4>Methods</h4>" + tags_html(project["methods"])
    extra = " featured-card" if project["featured"] else ""
    md(
        f"""
        <article class="card accent-card{extra}">
            <div class="eyebrow">Project {number:02d} / {text(project["category"])}</div>
            <h3>{text(project["title"])}</h3>
            <div class="meta">{text(project["period"])}</div>
            <p>{text(project["description"])}</p>
            {results_html(project["results"])}
            <h4>Work completed</h4>
            {bullets_html(project["bullets"])}
            {finding}
            {methods}
            <h4>Tools & topics</h4>
            {tags_html(project["tags"])}
            <div>{project_link}</div>
        </article>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# EXPERIENCE
# =========================================================
EXPERIENCE = [
    {
        "role": "Graduate Administrative Assistant",
        "organization": "Gallagher International Center — University of South Dakota",
        "dates": "August 2026 – Present",
        "short_dates": "Aug 2026 – Present",
        "location": "Vermillion, SD, USA",
        "type": "University",
        "bullets": [
            "Conduct mentoring and information sessions through GradRight for prospective and current students in India, explaining academic programs and university resources to diverse audiences.",
            "Develop and deliver informational content on Study Away, international education opportunities, program options, and application processes.",
            "Support planning and execution of international student programs, orientation, and fairs; maintain records using Microsoft Office and digital tools.",
        ],
        "tools": ["GradRight", "Microsoft Office", "Student mentoring", "Program planning"],
    },
    {
        "role": "International Office Student Assistant — Internship",
        "organization": "Gallagher International Center — University of South Dakota",
        "dates": "May 2026 – August 2026",
        "short_dates": "May – Aug 2026",
        "location": "Vermillion, SD, USA",
        "type": "University",
        "bullets": [
            "Supported Study Abroad and International Student Services with front desk operations, student guidance, and administrative tasks.",
            "Assisted in coordinating orientation programs and study abroad fairs; maintained accurate records and supported data entry using Microsoft Office tools.",
        ],
        "tools": ["Microsoft Office", "Data entry", "Event coordination"],
    },
    {
        "role": "Senior Analyst, DataScope Operations",
        "organization": "London Stock Exchange Group",
        "dates": "May 2022 – August 2025",
        "short_dates": "May 2022 – Aug 2025",
        "location": "Bangalore, India",
        "type": "Finance & Data",
        "bullets": [
            "Collaborated with financial and investment advisers and portfolio managers across brokerage houses, global banks, and investment institutions, providing specialised expertise in LSEG–Refinitiv products for advanced financial data analysis and presenting findings to non-technical clients.",
            "Used SQL to query a Numerical Data Architecture database for efficient retrieval of equity and fixed income data; defined best practices for the database and delivered product insights on DataScope Onsite and Refinitiv Eikon.",
            "Achieved a 10% reduction in customer complaints by introducing market-driven metrics to enhance the customer service support system.",
            "Recorded and managed problem incidents through the LSEG–Refinitiv CRM application and Salesforce, delivering solutions within prescribed SLAs and KPIs.",
            "Awarded the Q3 MDM Team Champion Award for team contribution, collaboration, and operational excellence within Data & Analytics Operations.",
        ],
        "tools": ["SQL", "Refinitiv Eikon", "DataScope Onsite", "Salesforce", "LSEG–Refinitiv CRM", "Equity data", "Fixed income data"],
    },
    {
        "role": "Associate, Accounts Payable",
        "organization": "Capgemini Technology Services",
        "dates": "April 2021 – May 2022",
        "short_dates": "Apr 2021 – May 2022",
        "location": "Bangalore, India",
        "type": "Finance & Data",
        "bullets": [
            "Managed invoice indexing and processing using Readsoft, Baseware, and SAP, consistently meeting daily targets within stipulated turnaround time (TAT).",
            "Facilitated timely audits within the invoice processing workflow to ensure process integrity, and collaborated with accounting and invoicing teams to resolve queries.",
            "Trained and mentored new hires, ensuring rapid onboarding and integration into the team.",
            "Received the Rising Star Award for outstanding performance and contributions to team success.",
        ],
        "tools": ["SAP", "Readsoft", "Baseware", "Invoice processing", "Audit support"],
    },
]


# =========================================================
# EDUCATION
# =========================================================
EDUCATION = [
    {
        "level": "Graduate education",
        "degree": "Master of Science in Business Analytics",
        "school": "University of South Dakota",
        "dates": "August 2025 – Present",
        "place": "United States",
        "gpa": "3.8 / 4.0",
        "coursework": [
            "Data Mining", "Quantitative Analysis", "Operational Analytics",
            "Data Management and Warehousing", "Business Analytics",
        ],
        "notes": [
            "Graduate projects: SPY options return prediction and optimisation (Operational Analytics) and NLP analysis of 10-K risk disclosures.",
        ],
    },
    {
        "level": "Undergraduate education",
        "degree": "Bachelor of Commerce",
        "school": "Bangalore University",
        "dates": "August 2017 – September 2020",
        "place": "India",
        "gpa": "3.9 / 4.0",
        "coursework": [
            "Quantitative Analysis for Business Decisions", "Financial Management",
            "Corporate Accounting", "Banking Law and Operations",
        ],
        "notes": [
            "Received the Quantitative Analysis for Business Decision Award for outstanding academic performance.",
        ],
    },
]


# =========================================================
# SKILLS AND CERTIFICATIONS
# =========================================================
SKILLS = {
    "Programming & Analytics": [
        "Python", "SQL", "R", "Predictive Modeling", "Time Series Forecasting",
        "Statistical Analysis", "Data Visualization",
    ],
    "Finance & Quantitative": [
        "Quantitative Analysis", "Financial Risk Analysis", "Financial Data Analysis",
        "Fixed Income", "Options Fundamentals", "Financial Markets",
    ],
    "Machine Learning & Optimisation": [
        "Linear Regression", "Random Forest", "Gradient Boosting", "Cross-Validation",
        "Linear Programming (lpSolve)", "Backtesting", "Sensitivity Analysis",
    ],
    "Time Series & Text Analytics": [
        "ARIMA", "Exponential Smoothing", "Nelson–Siegel", "TF-IDF", "Cosine Similarity",
        "LDA Topic Modeling", "Hierarchical Clustering", "Sentiment Analysis",
    ],
    "Tools & Platforms": [
        "Power BI", "Microsoft Excel", "Microsoft Word", "PowerPoint", "Outlook",
        "Google Sheets", "Google Docs", "Google Slides", "Salesforce CRM",
        "Refinitiv Eikon", "LSEG DataScope", "SAP", "ImageNow", "Perspective Content",
    ],
}

CERTIFICATIONS = [
    {"name": "Bloomberg Market Concepts (BMC)", "issuer": "Bloomberg"},
    {"name": "Bloomberg Finance Fundamentals (BFF)", "issuer": "Bloomberg"},
    {"name": "Bloomberg ESG Certificate (ESG)", "issuer": "Bloomberg"},
    {"name": "Bloomberg Spreadsheet Analysis — BQL (Bloomberg Query Language)", "issuer": "Bloomberg"},
    {"name": "Options 101 Certification", "issuer": "Akuna Capital"},
    {"name": "Options 201 Course — Completed", "issuer": "Akuna Capital"},
    {"name": "Coding for Data Certification", "issuer": "Coding for Data"},
    {"name": "DataScope QUEST ELITE Certification", "issuer": "London Stock Exchange Group"},
]

PUBLICATIONS = [
    "Business Opportunities in the Digital Era",
    "Recent Trends and Innovative Teaching Methodology in Higher Education",
]

PRESENTATIONS = [
    ("International Conference on Mind Power", "Free Thinking and Sustainability"),
    (
        "National Level Conference on Innovation and Sustainable Business Models",
        "Reshaping Business Opportunities in the Digital Era",
    ),
    (
        "National Level Conference on Connecting Young India and Global Market Opportunities for Sustainable Inclusive Growth",
        "Innovative Practices and Strategies in Commerce, Management, and Computer Applications in Current Global Scenario",
    ),
]

AWARDS = [
    (
        "Q3 MDM Team Champion Award — LSEG",
        "Recognised for exceptional team contribution, collaboration, and operational excellence within Data & Analytics Operations.",
    ),
    (
        "Rising Star Award — Capgemini",
        "Recognised for outstanding performance and contributions to team success.",
    ),
    (
        "Quantitative Analysis for Business Decision Award",
        "Recognised for outstanding academic performance and excellence in quantitative problem-solving.",
    ),
    (
        "Top 10 — Pre-University Program",
        "Graduated in the Top 10 with an outstanding score of 91%.",
    ),
]

INTERESTS = [
    "Business Analytics", "Financial Analyst", "Financial Data Analysis", "Data Analyst",
    "Risk Analytics", "Quantitative Research", "Market Data Analyst", "Data-driven Decision-making",
]


# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    md(
        f"""
        <div class="sidebar-monogram">{text(PROFILE["initials"])}</div>
        <div class="sidebar-name">{text(PROFILE["name"])}</div>
        <div class="sidebar-subtitle">{text(PROFILE["title"])}</div>
        <div class="sidebar-subtitle">{text(PROFILE["location"])}</div>
        """,
        unsafe_allow_html=True,
    )
    md(f"[{PROFILE['email']}](mailto:{PROFILE['email']})")
    md(f"[LinkedIn]({PROFILE['linkedin']}) · [GitHub]({PROFILE['github']})")
    resume_button("sidebar_resume")


# =========================================================
# HOME PAGE
# =========================================================
def home_page():
    left, right = st.columns([1.8, 1], gap="large")

    with left:
        md(
            f"""
            <div class="hero">
                <div class="eyebrow">Analytics · Finance · Data</div>
                <div class="hero-rule"></div>
                <h1>{text(PROFILE["name"])}</h1>
                <div class="hero-role">{text(PROFILE["title"])}</div>
                <p>
                    Business Analytics graduate student with 4+ years of experience in
                    financial data operations and quantitative analysis.
                </p>
                <p>
                    I connect financial market knowledge with statistical analysis,
                    predictive modeling, optimisation, and NLP — from SPY options to
                    Treasury yield curves and SEC risk disclosures.
                </p>
                <div class="hero-location">{text(PROFILE["location"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        resume_button("home_resume")
        social_links = link_html(PROFILE["linkedin"], "LinkedIn") + link_html(PROFILE["github"], "GitHub")
        if social_links:
            md(social_links, unsafe_allow_html=True)

    with right:
        show_photo()

    st.write("")

    # ---------------- About me (merged into Home) ----------------
    st.subheader("About me")
    left, right = st.columns(2, gap="large")
    with left:
        card("Professional summary", SUMMARY)
        card(
            "Finance experience meets analytical thinking",
            (
                "I am pursuing a Master of Science in Business Analytics at the University of "
                "South Dakota. Previously, I worked as a Senior Analyst in DataScope Operations "
                "at London Stock Exchange Group, supporting financial advisers, portfolio "
                "managers, global banks, and institutional clients."
            ),
        )
    with right:
        card(
            "What I bring",
            bullets=[
                "Experience working with equity and fixed income data and LSEG–Refinitiv products.",
                "SQL-based data retrieval, analytical problem-solving, and client communication within SLAs and KPIs.",
                "End-to-end analytics in R and Python: descriptive, predictive, and prescriptive modeling.",
                "Hands-on projects in SPY options, SEC 10-K text analytics, financial risk, Bitcoin and gold forecasting, and Treasury yield curves.",
                "A strong interest in quantitative finance, risk analytics, and data-driven decisions.",
            ],
        )
        card(
            "My focus",
            "Financial data analysis, risk analytics, time series forecasting, fixed income, derivatives, and quantitative finance.",
            tags=["Python", "SQL", "R", "Financial Markets", "Predictive Modeling", "NLP"],
        )

    timeline = "".join(
        f"""
        <div class="timeline-item">
            <div class="timeline-date">{text(job["short_dates"])}</div>
            <div>
                <div class="timeline-role">{text(job["role"])}</div>
                <div class="timeline-org">{text(job["organization"])} · {text(job["location"])}</div>
            </div>
        </div>
        """
        for job in EXPERIENCE
    )
    timeline += """
        <div class="timeline-item">
            <div class="timeline-date">Aug 2025 – Present</div>
            <div><div class="timeline-role">MS in Business Analytics</div>
            <div class="timeline-org">University of South Dakota · GPA 3.8 / 4.0</div></div>
        </div>
        <div class="timeline-item">
            <div class="timeline-date">Aug 2017 – Sep 2020</div>
            <div><div class="timeline-role">Bachelor of Commerce</div>
            <div class="timeline-org">Bangalore University · GPA 3.9 / 4.0</div></div>
        </div>
    """

    email = text(PROFILE["email"])
    details = [
        ("Name", text(PROFILE["name"])),
        ("Location", text(PROFILE["location"])),
        ("Email", f'<a href="mailto:{email}">{email.replace("@", "@<wbr>")}</a>'),
        ("Current study", "MS in Business Analytics"),
    ]
    if PROFILE["phone"]:
        details.append(("Phone", text(PROFILE["phone"])))

    left, right = st.columns([1, 1], gap="large")
    with left:
        md(f'<div class="card"><h3>Career timeline</h3>{timeline}</div>')
    with right:
        md(f'<div class="card"><h3>Profile details</h3>{detail_rows(details)}</div>')


# =========================================================
# PROJECTS PAGE
# =========================================================
def projects_page():
    heading(
        "Projects",
        "Options analytics, NLP on SEC filings, financial risk, time series forecasting, and fixed income.",
    )

    filter_col, search_col = st.columns([1, 1.6])
    with filter_col:
        selected = st.selectbox("Filter projects by area", options=PROJECT_CATEGORIES, key="project_filter")
    with search_col:
        query = st.text_input(
            "Search projects",
            placeholder="e.g. ARIMA, LDA, gradient boosting",
            key="project_search",
        ).strip().lower()

    def matches(project):
        if selected != "All" and project["category"] != selected:
            return False
        if not query:
            return True
        blob = " ".join(
            [project["title"], project["description"], " ".join(project["bullets"]),
             project["finding"], " ".join(project["methods"]), " ".join(project["tags"])]
        ).lower()
        return query in blob

    visible = [(i, p) for i, p in enumerate(PROJECTS, start=1) if matches(p)]

    if not visible:
        st.info("No projects match that filter. Try a different area or search term.")
        return

    st.caption(f"Showing {len(visible)} of {len(PROJECTS)} projects")

    featured = [(n, p) for n, p in visible if p["featured"]]
    others = [(n, p) for n, p in visible if not p["featured"]]

    for number, project in featured:
        project_card(number, project)

    columns = st.columns(2)
    for position, (number, project) in enumerate(others):
        with columns[position % 2]:
            project_card(number, project)


# =========================================================
# EXPERIENCE PAGE
# =========================================================
def experience_page():
    heading("Experience", "Financial data operations, client support, and university service.")

    stat_row([
        ("3+ years", "LSEG — DataScope Operations"),
        ("1+ year", "Capgemini — Accounts Payable"),
        ("10%", "Fewer customer complaints at LSEG"),
        ("2", "Workplace awards"),
    ])

    view = st.radio(
        "Show",
        ["All roles", "Finance & Data", "University"],
        horizontal=True,
        key="experience_view",
    )

    for job in EXPERIENCE:
        if view != "All roles" and job["type"] != view:
            continue
        md(
            f"""
            <div class="card accent-card">
                <h3>{text(job["role"])}</h3>
                <div class="organization">{text(job["organization"])}</div>
                <div class="meta">{text(job["dates"])} · {text(job["location"])}</div>
                {bullets_html(job["bullets"])}
                <h4>Tools & skills</h4>
                {tags_html(job["tools"])}
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# EDUCATION PAGE
# =========================================================
def education_page():
    heading("Education", "Academic background, relevant coursework, and academic recognition.")

    for ed in EDUCATION:
        notes = bullets_html(ed["notes"]) if ed["notes"] else ""
        md(
            f"""
            <div class="card accent-card">
                <div class="eyebrow">{text(ed["level"])}</div>
                <h3>{text(ed["degree"])}</h3>
                <div class="organization">{text(ed["school"])}</div>
                <div class="meta">{text(ed["dates"])} · {text(ed["place"])}</div>
                <p>Overall GPA: <b>{text(ed["gpa"])}</b></p>
                <h4>Relevant coursework</h4>
                {tags_html(ed["coursework"])}
                <h4>Highlights</h4>
                {notes}
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# SKILLS AND CERTIFICATIONS PAGE
# =========================================================
def skills_page():
    heading(
        "Skills & certifications",
        "Analytical capabilities, financial knowledge, and professional learning.",
    )

    left, right = st.columns(2, gap="large")
    for index, (category, items) in enumerate(SKILLS.items()):
        with (left if index % 2 == 0 else right):
            card(category, tags=items)

    st.subheader("Certifications & completed courses")
    issuers = []
    for cert in CERTIFICATIONS:
        if cert["issuer"] not in issuers:
            issuers.append(cert["issuer"])

    columns = st.columns(2)
    for index, issuer in enumerate(issuers):
        names = [c["name"] for c in CERTIFICATIONS if c["issuer"] == issuer]
        with columns[index % 2]:
            card(issuer, bullets=names, extra_class="accent-card")


# =========================================================
# RESEARCH AND ACHIEVEMENTS PAGE
# =========================================================
def research_page():
    heading(
        "Research & achievements",
        "Published papers, conference presentations, and professional recognition.",
    )

    stat_row([
        (str(len(PUBLICATIONS)), "Published research papers"),
        (str(len(PRESENTATIONS)), "Conference paper presentations"),
        (str(len(AWARDS)), "Awards and achievements"),
    ])

    card("Published research papers", bullets=PUBLICATIONS, extra_class="accent-card")

    st.subheader("Conference presentations")
    for conference, paper in PRESENTATIONS:
        card(conference, f"Paper: “{paper}”")

    st.subheader("Awards & achievements")
    columns = st.columns(2)
    for index, (title, description) in enumerate(AWARDS):
        with columns[index % 2]:
            card(title, description, extra_class="accent-card")


# =========================================================
# CONTACT PAGE
# =========================================================
def contact_page():
    heading("Contact", "Connect about analytics, financial data, and quantitative work.")

    card("Roles I'm interested in", tags=INTERESTS)

    email = text(PROFILE["email"])
    rows = [
        ("Email", f'<a href="mailto:{email}">{email.replace("@", "@<wbr>")}</a>'),
        ("Location", text(PROFILE["location"])),
    ]
    if PROFILE.get("phone"):
        rows.append(("Phone", text(PROFILE["phone"])))

    social_links = link_html(PROFILE.get("linkedin", ""), "LinkedIn") + link_html(PROFILE.get("github", ""), "GitHub")

    left, right = st.columns([1, 1], gap="large")
    with left:
        md(
            f"""
            <div class="card accent-card">
                <h3>Get in touch</h3>
                {detail_rows(rows)}
                <div style="margin-top: 8px;">{social_links}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        resume_button("contact_resume")

    with right:
        with st.form("contact_form", clear_on_submit=False):
            md("**Send me a message**")
            sender = st.text_input("Your name", key="contact_name")
            sender_email = st.text_input("Your email", key="contact_email")
            message = st.text_area("Message", key="contact_message", height=140)
            submitted = st.form_submit_button("Prepare email")

        if submitted:
            if not (sender.strip() and sender_email.strip() and message.strip()):
                st.warning("Please fill in your name, email, and message.")
            else:
                from urllib.parse import quote

                subject = quote(f"Portfolio enquiry from {sender.strip()}")
                body = quote(f"{message.strip()}\n\n— {sender.strip()} ({sender_email.strip()})")
                st.success("Your email is ready to send.")
                st.link_button(
                    "Open in your email app",
                    f"mailto:{PROFILE['email']}?subject={subject}&body={body}",
                )


# =========================================================
# MULTIPAGE NAVIGATION
# =========================================================
pages = [
    st.Page(home_page, title="Home", default=True),
    st.Page(projects_page, title="Projects", url_path="projects"),
    st.Page(experience_page, title="Experience", url_path="experience"),
    st.Page(education_page, title="Education", url_path="education"),
    st.Page(skills_page, title="Skills & Certifications", url_path="skills"),
    st.Page(research_page, title="Research & Achievements", url_path="research"),
    st.Page(contact_page, title="Contact", url_path="contact"),
]

navigation = st.navigation(pages, position="top")
navigation.run()


# =========================================================
# FOOTER
# =========================================================
md(
    f"""
    <div class="footer">
        {text(PROFILE["name"])} · Business Analytics & Financial Data
        <br>
        Built with Python and Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)

