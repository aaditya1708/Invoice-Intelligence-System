import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Invoice Intelligence System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CUSTOM CSS — Light Theme
# ==========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Background ── */
.stApp {
    background: #0D1424;
    color: #E4E9F5;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #090F1D !important;
    border-right: 1px solid #1E2A45;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #93A5CC !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace !important;
}

[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #131C33 !important;
    border: 1px solid #29365A !important;
    border-radius: 8px !important;
    color: #E4E9F5 !important;
}

/* ── Sidebar Brand ── */
.sidebar-brand {
    padding: 1.5rem 0 1.8rem 0;
    border-bottom: 1px solid #1E2A45;
    margin-bottom: 1.5rem;
}
.sidebar-brand .logo-icon { font-size: 2.2rem; margin-bottom: 0.4rem; }
.sidebar-brand .logo-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    color: #60A5FA;
    letter-spacing: 0.16em;
    text-transform: uppercase;
}
.sidebar-brand .logo-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.25;
    margin-top: 0.2rem;
}
.sidebar-status {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #6EE7B7;
    margin-top: 0.75rem;
}
.sidebar-status .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #6EE7B7;
    box-shadow: 0 0 6px #6EE7B7;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.35; }
}

/* ── Page Header ── */
.page-header {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 2rem 0 1.4rem 0;
    border-bottom: 2px solid #1E2A45;
    margin-bottom: 2rem;
}
.page-header .header-icon { font-size: 2.4rem; line-height: 1; margin-top: 0.1rem; }
.page-header .header-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    color: #60A5FA;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 0.2rem;
}
.page-header .header-title {
    font-size: 1.7rem;
    font-weight: 700;
    color: #F1F5FB;
    letter-spacing: -0.02em;
    line-height: 1.1;
}
.page-header .header-desc {
    font-size: 0.85rem;
    color: #93A5CC;
    margin-top: 0.3rem;
}

/* ── Form Card ── */
.form-card {
    background: #131C33;
    border: 1px solid #29365A;
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.25);
}
.form-card-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    color: #93A5CC;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 1.1rem;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid #232F4E;
}

/* ── Input Fields ── */
.stNumberInput label,
.stSelectbox label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem !important;
    font-weight: 600 !important;
    color: #93A5CC !important;
    letter-spacing: 0.07em !important;
    text-transform: uppercase !important;
}

.stNumberInput input {
    background: #0D1424 !important;
    border: 1.5px solid #29365A !important;
    border-radius: 8px !important;
    color: #E4E9F5 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 0.85rem !important;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.stNumberInput input:focus {
    border-color: #60A5FA !important;
    box-shadow: 0 0 0 3px rgba(96,165,250,0.15) !important;
    background: #131C33 !important;
}

.stSelectbox > div > div {
    background: #0D1424 !important;
    border: 1.5px solid #29365A !important;
    border-radius: 8px !important;
    color: #E4E9F5 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 500 !important;
}

/* ── Button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #1D4ED8 0%, #2563EB 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.8rem 1.5rem !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    margin-top: 0.4rem !important;
    box-shadow: 0 4px 14px rgba(37,99,235,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(37,99,235,0.4) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result: Freight ── */
.result-freight {
    background: linear-gradient(135deg, #142038 0%, #16294A 100%);
    border: 1.5px solid #2E4B7D;
    border-radius: 14px;
    padding: 2rem 1.5rem;
    text-align: center;
    margin-top: 1rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.result-freight::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #1D4ED8, #3B82F6, #93C5FD);
    border-radius: 14px 14px 0 0;
}
.result-freight .result-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    color: #60A5FA;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.result-freight .result-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.8rem;
    font-weight: 700;
    color: #E4E9F5;
    letter-spacing: -0.02em;
    line-height: 1;
}
.result-freight .result-sub {
    font-size: 0.75rem;
    color: #7CB3F7;
    margin-top: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.05em;
}

/* ── Result: High Risk ── */
.result-risk-high {
    background: linear-gradient(135deg, #331418 0%, #3D1519 100%);
    border: 1.5px solid #7A2E32;
    border-radius: 14px;
    padding: 2rem 1.5rem;
    text-align: center;
    margin-top: 1rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.result-risk-high::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #991B1B, #EF4444, #FCA5A5);
    border-radius: 14px 14px 0 0;
}
.result-risk-high .risk-icon { font-size: 2.2rem; margin-bottom: 0.4rem; }
.result-risk-high .risk-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    color: #F87171;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.result-risk-high .risk-value {
    font-size: 1.45rem;
    font-weight: 700;
    color: #FEE2E2;
}
.result-risk-high .risk-desc {
    font-size: 0.8rem;
    color: #FCA5A5;
    margin-top: 0.5rem;
    line-height: 1.5;
}

/* ── Result: Low Risk ── */
.result-risk-low {
    background: linear-gradient(135deg, #0F2B1E 0%, #113322 100%);
    border: 1.5px solid #276B49;
    border-radius: 14px;
    padding: 2rem 1.5rem;
    text-align: center;
    margin-top: 1rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.result-risk-low::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #047857, #10B981, #6EE7B7);
    border-radius: 14px 14px 0 0;
}
.result-risk-low .risk-icon { font-size: 2.2rem; margin-bottom: 0.4rem; }
.result-risk-low .risk-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    font-weight: 600;
    color: #6EE7B7;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.result-risk-low .risk-value {
    font-size: 1.45rem;
    font-weight: 700;
    color: #DCFCE7;
}
.result-risk-low .risk-desc {
    font-size: 0.8rem;
    color: #86EFAC;
    margin-top: 0.5rem;
    line-height: 1.5;
}

/* ── Awaiting state ── */
.awaiting-box {
    background: #131C33;
    border: 1.5px dashed #29365A;
    border-radius: 14px;
    padding: 3rem 2rem;
    text-align: center;
    margin-top: 1rem;
}
.awaiting-box .aw-icon { font-size: 2.2rem; opacity: 0.5; margin-bottom: 0.7rem; }
.awaiting-box .aw-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    color: #93A5CC;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.awaiting-box .aw-sub {
    font-size: 0.8rem;
    color: #5A6B94;
    margin-top: 0.3rem;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: #131C33;
    border: 1px solid #232F4E;
    border-radius: 10px;
    padding: 0.9rem 1.1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.2);
}
[data-testid="stMetricLabel"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.62rem !important;
    color: #93A5CC !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    color: #E4E9F5 !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
}

/* ── Chrome cleanup ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 2rem !important;
    max-width: 1100px;
}
[data-testid="column"] { padding: 0 0.4rem; }
</style>
""", unsafe_allow_html=True)


# ==========================
# LOAD MODELS
# ==========================

@st.cache_resource
def load_models():
    
    freight_model = joblib.load("freight_model.pkl")
    freight_preprocessor = joblib.load("freight_model_preprocessing.pkl")
    risk_model = joblib.load("risk_model.pkl")
    risk_preprocessor = joblib.load("risk_model_preprocessing.pkl")
    return freight_model, freight_preprocessor, risk_model, risk_preprocessor

freight_model, freight_preprocessor, risk_model, risk_preprocessor = load_models()


# ==========================
# SIDEBAR
# ==========================

with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="logo-icon">🧠</div>
        <div class="logo-eyebrow">Invoice Intelligence</div>
        <div class="logo-title">AI Prediction<br>System</div>
        <div class="sidebar-status">
            <div class="dot"></div> Models ready
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="font-family:JetBrains Mono,monospace;font-size:0.6rem;color:#5B8CBF;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.4rem;">Prediction Mode</p>', unsafe_allow_html=True)

    option = st.selectbox(
        "",
        ["Freight Cost Prediction", "Invoice Risk Prediction"],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'JetBrains Mono',monospace;font-size:0.6rem;color:#2D5A8E;border-top:1px solid #2D5A8E;padding-top:1rem;letter-spacing:0.06em;line-height:1.8;">
        v1.0.0 · Invoice Intelligence<br>Supply Chain Analytics
    </div>
    """, unsafe_allow_html=True)


# ==========================
# MONTH NAMES
# ==========================

MONTH_NAMES = {
    1:"January", 2:"February", 3:"March", 4:"April",
    5:"May", 6:"June", 7:"July", 8:"August",
    9:"September", 10:"October", 11:"November", 12:"December"
}


# ==================================================
# FREIGHT COST PREDICTION
# ==================================================

if option == "Freight Cost Prediction":

    st.markdown("""
    <div class="page-header">
        <div class="header-icon">🚚</div>
        <div>
            <div class="header-eyebrow">Predictive Analytics</div>
            <div class="header-title">Freight Cost Prediction</div>
            <div class="header-desc">Enter vendor and order details to estimate the freight cost for this shipment.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_form, col_result = st.columns([1.1, 0.9], gap="large")

    with col_form:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<div class="form-card-title">Vendor & Order Details</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            dollars = st.number_input("Invoice Value (USD)", min_value=0.0, step=0.01, format="%.2f")
            quantity = st.number_input("Quantity", min_value=0, step=1)
            num_products = st.number_input("No. of Products", min_value=0, step=1)
        with col2:
            avg_purchase_price = st.number_input("Avg. Purchase Price", min_value=0.0, step=0.01, format="%.2f")
            num_brands = st.number_input("No. of Brands", min_value=0, step=1)

        st.markdown('</div>', unsafe_allow_html=True)
        predict_freight = st.button("⚡  Calculate Freight Cost", use_container_width=True)

    with col_result:
        st.markdown("<br><br>", unsafe_allow_html=True)

        if predict_freight:
            input_df = pd.DataFrame({
                "Quantity": [quantity],
                "Dollars": [dollars],
                "Avg_PurchasePrice": [avg_purchase_price],
                "Num_Products": [num_products],
                "Num_Brands": [num_brands]
            })
            processed_data = freight_preprocessor.transform(input_df)
            prediction = freight_model.predict(processed_data)
            cost = prediction[0]

            st.markdown(f"""
            <div class="result-freight">
                <div class="result-label">Estimated Freight Cost</div>
                <div class="result-value">${cost:,.2f}</div>
                <div class="result-sub">USD · Single Invoice · AI Predicted</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                margin_pct = (cost / dollars * 100) if dollars > 0 else 0
                st.metric("Freight-to-Value", f"{margin_pct:.1f}%")
            with c2:
                per_unit = (cost / quantity) if quantity > 0 else 0
                st.metric("Cost per Unit", f"${per_unit:.2f}")
        else:
            st.markdown("""
            <div class="awaiting-box">
                <div class="aw-icon">📦</div>
                <div class="aw-label">Awaiting Input</div>
                <div class="aw-sub">Fill in the form and click Calculate</div>
            </div>
            """, unsafe_allow_html=True)


# ==================================================
# INVOICE RISK PREDICTION
# ==================================================

else:

    st.markdown("""
    <div class="page-header">
        <div class="header-icon">⚠️</div>
        <div>
            <div class="header-eyebrow">Risk Assessment</div>
            <div class="header-title">Invoice Risk Prediction</div>
            <div class="header-desc">Analyse invoice parameters to detect high-risk transactions before processing.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_form, col_result = st.columns([1.1, 0.9], gap="large")

    with col_form:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<div class="form-card-title">Vendor & Order Details</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input("Quantity", min_value=0, step=1, key="risk_qty")
            avg_purchase_price = st.number_input("Avg. Purchase Price", min_value=0.0, step=0.01, format="%.2f", key="risk_avg_price")
            num_products = st.number_input("No. of Products", min_value=0, step=1, key="risk_products")
        with col2:
            po_number = st.number_input("PO Number", min_value=0, step=1, key="risk_po")
            dollars = st.number_input("Invoice Value (USD)", min_value=0.0, step=0.01, format="%.2f", key="risk_dollars")
            freight = st.number_input("Freight Amount", min_value=0.0, step=0.01, format="%.2f", key="risk_freight")
            num_brands = st.number_input("No. of Brands", min_value=0, step=1, key="risk_brands")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        st.markdown('<div class="form-card-title">Invoice Timeline</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            invoice_month = st.selectbox("Invoice Month", list(range(1, 13)), format_func=lambda x: MONTH_NAMES[x])
        with col2:
            po_month = st.selectbox("PO Month", list(range(1, 13)), format_func=lambda x: MONTH_NAMES[x])
        with col3:
            pay_month = st.selectbox("Payment Month", list(range(1, 13)), format_func=lambda x: MONTH_NAMES[x])
        st.markdown('</div>', unsafe_allow_html=True)

        predict_risk = st.button("🔍  Assess Invoice Risk", use_container_width=True)

    with col_result:
        st.markdown("<br><br>", unsafe_allow_html=True)

        if predict_risk:
            input_df = pd.DataFrame({
                "PONumber": [po_number],
                "Quantity": [quantity],
                "Dollars": [dollars],
                "Freight": [freight],
                "Avg_PurchasePrice": [avg_purchase_price],
                "Num_Products": [num_products],
                "Num_Brands": [num_brands],
                "InvoiceMonth": [invoice_month],
                "POMonth": [po_month],
                "PayMonth": [pay_month]
            })
            processed_data = risk_preprocessor.transform(input_df)
            prediction = risk_model.predict(processed_data)

            if prediction[0] == 1:
                st.markdown("""
                <div class="result-risk-high">
                    <div class="risk-icon">🔴</div>
                    <div class="risk-label">Risk Classification</div>
                    <div class="risk-value">High Risk Invoice</div>
                    <div class="risk-desc">This invoice shows anomalous patterns.<br>Manual review is recommended.</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="result-risk-low">
                    <div class="risk-icon">🟢</div>
                    <div class="risk-label">Risk Classification</div>
                    <div class="risk-value">Low Risk Invoice</div>
                    <div class="risk-desc">This invoice appears within normal parameters.<br>Safe to proceed with processing.</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            delay = pay_month - invoice_month if pay_month >= invoice_month else (12 - invoice_month + pay_month)
            po_gap = invoice_month - po_month if invoice_month >= po_month else (12 - po_month + invoice_month)
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Payment Lag", f"{delay} mo")
            with c2:
                st.metric("PO → Invoice Gap", f"{po_gap} mo")
        else:
            st.markdown("""
            <div class="awaiting-box">
                <div class="aw-icon">🔍</div>
                <div class="aw-label">Awaiting Input</div>
                <div class="aw-sub">Fill in the form and click Assess Risk</div>
            </div>
            """, unsafe_allow_html=True)