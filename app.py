import streamlit as st

from ticket_automation import generate_ticket_response
from knowledge_base import get_microsoft_articles


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Customer Support Ticket Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>
        .main {
            padding-top: 1.5rem;
        }

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .hero {
            padding: 2rem 2.2rem;
            border-radius: 20px;
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%);
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.18);
        }

        .hero h1 {
            margin: 0;
            font-size: 2.25rem;
            font-weight: 750;
            letter-spacing: -0.5px;
        }

        .hero p {
            margin: 0.55rem 0 0;
            font-size: 1.05rem;
            opacity: 0.92;
        }

        .hero .creator {
            margin-top: 1rem;
            font-size: 0.88rem;
            opacity: 0.82;
        }

        .section-title {
            font-size: 1.2rem;
            font-weight: 700;
            margin-top: 1.25rem;
            margin-bottom: 0.65rem;
        }

        .result-card {
            padding: 1.15rem 1.25rem;
            border: 1px solid rgba(148, 163, 184, 0.28);
            border-radius: 15px;
            background: rgba(248, 250, 252, 0.72);
            min-height: 105px;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
        }

        .result-label {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.65px;
            color: #64748b;
            margin-bottom: 0.45rem;
        }

        .result-value {
            font-size: 1.08rem;
            font-weight: 700;
            color: #0f172a;
            word-break: break-word;
        }

        .content-card {
            padding: 1.25rem 1.35rem;
            border: 1px solid rgba(148, 163, 184, 0.28);
            border-radius: 15px;
            background: white;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.045);
            margin-bottom: 0.85rem;
        }

        .article-card {
            padding: 1rem 1.15rem;
            border-left: 4px solid #2563eb;
            border-radius: 10px;
            background: #f8fafc;
            margin-bottom: 0.8rem;
        }

        .article-title {
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.25rem;
        }

        .article-subtitle {
            font-size: 0.82rem;
            color: #64748b;
        }

        .response-card {
            padding: 1.3rem 1.4rem;
            border-radius: 15px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            line-height: 1.65;
            color: #1e293b;
        }

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 0.8rem;
            padding-top: 1.5rem;
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(148, 163, 184, 0.28);
            border-radius: 15px;
            padding: 0.85rem 1rem;
            background: white;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.045);
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 700;
            min-height: 2.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <h1>🤖 AI Customer Support Ticket Analyzer</h1>
        <p>
            Intelligent IT support classification, automation and
            Microsoft knowledge-base assistance.
        </p>
        <div class="creator">
            Built by <strong>Zeeshan Hassan</strong>
            &nbsp;•&nbsp; Python
            &nbsp;•&nbsp; AI Automation
            &nbsp;•&nbsp; Microsoft 365
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# TICKET INPUT
# ============================================================

st.markdown('<div class="section-title">🎫 Support Ticket</div>', unsafe_allow_html=True)

ticket = st.text_area(
    "Describe the customer's issue",
    placeholder="Example: I cannot log into Outlook because MFA keeps failing.",
    height=145,
    label_visibility="collapsed",
)

analyze = st.button(
    "🔍  Analyze Ticket",
    type="primary",
    use_container_width=True,
)


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not ticket.strip():
        st.warning("Please enter a support ticket before starting the analysis.")

    else:
        with st.spinner("Analyzing ticket and finding relevant Microsoft resources..."):

            result = generate_ticket_response(ticket)

            articles = get_microsoft_articles(
                result["category"],
                result["issue_type"],
            )

        st.success("Ticket analysis completed successfully.")

        # ====================================================
        # CLASSIFICATION
        # ====================================================

        st.markdown(
            '<div class="section-title">📊 Ticket Classification</div>',
            unsafe_allow_html=True,
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Category</div>
                    <div class="result-value">📁 {result["category"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Issue Type</div>
                    <div class="result-value">🧩 {result["issue_type"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col3:
            priority_icon = "🔴" if result["priority"] == "High" else "🟡" if result["priority"] == "Medium" else "🟢"

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Priority</div>
                    <div class="result-value">{priority_icon} {result["priority"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col4:
            sentiment_icon = "🔴" if result["sentiment"] == "NEGATIVE" else "🟢"

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-label">Sentiment</div>
                    <div class="result-value">{sentiment_icon} {result["sentiment"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ====================================================
        # ROOT CAUSE / RECOMMENDED ACTION
        # ====================================================

        st.markdown(
            '<div class="section-title">🔎 Troubleshooting Assessment</div>',
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="content-card">
                    <h4>🔎 Root Cause</h4>
                    <p>{result["root_cause"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                f"""
                <div class="content-card">
                    <h4>🛠️ Recommended Action</h4>
                    <p>{result["recommended_action"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ====================================================
        # MICROSOFT KNOWLEDGE BASE
        # ====================================================

        st.markdown(
            '<div class="section-title">📚 Recommended Microsoft Resources</div>',
            unsafe_allow_html=True,
        )

        if articles:

            st.caption(
                f"{len(articles)} relevant Microsoft Learn resource(s) "
                "matched to the ticket classification."
            )

            for index, article in enumerate(articles, start=1):

                st.markdown(
                    f"""
                    <div class="article-card">
                        <div class="article-title">
                            {index}. {article["title"]}
                        </div>
                        <div class="article-subtitle">
                            Official Microsoft Learn resource
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.link_button(
                    "📖  Read Microsoft Article",
                    article["url"],
                    use_container_width=False,
                )

        else:
            st.info(
                "No specific Microsoft knowledge-base articles were found "
                "for this ticket."
            )

        # ====================================================
        # CUSTOMER RESPONSE
        # ====================================================

        st.markdown(
            '<div class="section-title">💬 Suggested Customer Response</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="response-card">
                {result["customer_response"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ====================================================
        # AUTOMATION ASSESSMENT
        # ====================================================

        st.markdown(
            '<div class="section-title">⚙️ Automation Assessment</div>',
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Quality Score",
                f'{result["quality_score"]}/100',
            )

        with col2:
            human_review = result["human_required"]

            st.metric(
                "Human Review",
                human_review,
            )

        if human_review == "YES":
            st.warning(
                "Human review is recommended before using this response "
                "for a real customer case."
            )
        else:
            st.success(
                "This ticket is suitable for automated handling based "
                "on the current assessment."
            )

        st.divider()

        st.caption(
            "AI-assisted support analysis. Review results before using "
            "them for real customer cases."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        AI Customer Support Ticket Analyzer
        &nbsp;•&nbsp;
        Built by Zeeshan Hassan
        &nbsp;•&nbsp;
        Python | AI Automation | Microsoft 365
    </div>
    """,
    unsafe_allow_html=True,
)
