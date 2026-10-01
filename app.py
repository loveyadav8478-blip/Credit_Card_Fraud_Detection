import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SecurePay - Fraud Detection",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PROFESSIONAL DARK THEME
# ============================================================

st.markdown("""
<style>

/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background: #0b1120;
    color: #e5e7eb;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ============================================================
   HEADER
   ============================================================ */

.header {
    background: linear-gradient(
        135deg,
        #172033 0%,
        #1e293b 100%
    );

    padding: 30px 32px;
    border-radius: 16px;

    border: 1px solid #273449;

    margin-bottom: 22px;
}

.header-title {
    color: #f8fafc;
    font-size: 32px;
    font-weight: 700;
    margin: 0;
}

.header-subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-top: 8px;
}


/* ============================================================
   INFO MESSAGE
   ============================================================ */

div[data-testid="stAlert"] {
    border-radius: 10px;
}


/* ============================================================
   SECTION CARDS
   ============================================================ */

.section {
    background: #111827;

    padding: 22px;

    border-radius: 14px;

    border: 1px solid #273449;

    margin-bottom: 20px;
}

.section-title {
    color: #f8fafc;

    font-size: 20px;

    font-weight: 650;

    margin-bottom: 5px;
}

.section-description {
    color: #94a3b8;

    font-size: 14px;
}


/* ============================================================
   INPUT LABELS
   ============================================================ */

.stNumberInput label,
.stSelectbox label {
    color: #cbd5e1 !important;

    font-size: 13px !important;

    font-weight: 500 !important;
}


/* ============================================================
   NUMBER INPUTS
   ============================================================ */

.stNumberInput input {
    background-color: #171d2b !important;

    color: #f8fafc !important;

    border: 1px solid #30394d !important;

    border-radius: 8px !important;
}


/* ============================================================
   SELECT BOX
   ============================================================ */

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #171d2b !important;

    color: #f8fafc !important;

    border: 1px solid #30394d !important;

    border-radius: 8px !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {

    background: linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 9px !important;

    height: 48px !important;

    font-size: 15px !important;

    font-weight: 600 !important;

    transition: all 0.2s ease;
}

.stButton > button:hover {

    background: linear-gradient(
        135deg,
        #3b82f6,
        #2563eb
    ) !important;

    transform: translateY(-1px);

}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border-color: #273449 !important;
}


/* ============================================================
   RESULT CARD
   ============================================================ */

.result-box {

    background: linear-gradient(
        135deg,
        #111827,
        #172033
    );

    padding: 30px;

    border-radius: 16px;

    border: 1px solid #334155;

    text-align: center;

    margin-top: 25px;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.25);
}

.result-title {

    color: #f8fafc;

    font-size: 25px;

    font-weight: 700;

    margin-bottom: 8px;
}

.result-probability {

    color: #60a5fa;

    font-size: 44px;

    font-weight: 750;

    margin: 8px 0;
}

.result-description {

    color: #94a3b8;

    font-size: 14px;
}


/* ============================================================
   RISK ASSESSMENT
   ============================================================ */

.risk-title {

    color: #f8fafc;

    font-size: 20px;

    font-weight: 650;

    margin-top: 25px;

    margin-bottom: 10px;
}


/* ============================================================
   PROGRESS BAR
   ============================================================ */

.stProgress > div > div > div > div {
    background: #2563eb !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    text-align: center;

    color: #64748b;

    font-size: 12px;

    margin-top: 40px;

    padding-top: 20px;

    border-top: 1px solid #1e293b;
}


/* ============================================================
   HIDE STREAMLIT BRANDING
   ============================================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #0b1120;
}

::-webkit-scrollbar-thumb {
    background: #334155;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #475569;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load("model/fraud_model.pkl")

    config = joblib.load("model/model_config.pkl")

    return model, config


try:

    model, config = load_model()

    threshold = config["threshold"]

    features = config["features"]

except Exception:

    st.error(
        "Unable to load the transaction security system. "
        "Please verify that the model files are available."
    )

    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header">

    <div class="header-title">
        💳 SecurePay
    </div>

    <div class="header-subtitle">
        Credit Card Transaction Security
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRODUCTION
# ============================================================

st.info(
    "Enter the transaction details below to assess its "
    "potential fraud risk."
)


# ============================================================
# TRANSACTION INFORMATION
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Transaction Information
    </div>

    <div class="section-description">
        Provide the location and purchase information associated
        with this transaction.
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# LOCATION AND PURCHASE FEATURES
# ============================================================

col1, col2 = st.columns(2)


with col1:

    distance_from_home = st.number_input(
        "Distance from home",
        min_value=0.0,
        value=10.0,
        step=0.1,
        help=(
            "Distance between the transaction location "
            "and the customer's home."
        )
    )


with col2:

    distance_from_last_transaction = st.number_input(
        "Distance from previous transaction",
        min_value=0.0,
        value=5.0,
        step=0.1,
        help=(
            "Distance between the current transaction "
            "and the previous transaction."
        )
    )


col3, col4 = st.columns(2)


with col3:

    ratio_to_median_purchase_price = st.number_input(
        "Purchase amount ratio",
        min_value=0.0,
        value=1.0,
        step=0.01,
        help=(
            "Current purchase amount relative to "
            "the customer's typical purchase amount."
        )
    )


with col4:

    repeat_retailer = st.selectbox(
        "Previous purchase from retailer",
        options=[0, 1],
        format_func=lambda x: (
            "Yes" if x == 1 else "No"
        )
    )


# ============================================================
# TRANSACTION METHOD
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Transaction Method
    </div>

    <div class="section-description">
        Select how this transaction was processed.
    </div>

</div>
""", unsafe_allow_html=True)


col5, col6, col7 = st.columns(3)


with col5:

    used_chip = st.selectbox(
        "Chip used",
        options=[0, 1],
        format_func=lambda x: (
            "Yes" if x == 1 else "No"
        )
    )


with col6:

    used_pin_number = st.selectbox(
        "PIN used",
        options=[0, 1],
        format_func=lambda x: (
            "Yes" if x == 1 else "No"
        )
    )


with col7:

    online_order = st.selectbox(
        "Online transaction",
        options=[0, 1],
        format_func=lambda x: (
            "Yes" if x == 1 else "No"
        )
    )


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.write("")

check_transaction = st.button(
    "🔍  Assess Transaction",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if check_transaction:

    # --------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame([
        {
            "distance_from_home":
                distance_from_home,

            "distance_from_last_transaction":
                distance_from_last_transaction,

            "ratio_to_median_purchase_price":
                ratio_to_median_purchase_price,

            "repeat_retailer":
                repeat_retailer,

            "used_chip":
                used_chip,

            "used_pin_number":
                used_pin_number,

            "online_order":
                online_order
        }
    ])


    # --------------------------------------------------------
    # ENSURE CORRECT FEATURE ORDER
    # --------------------------------------------------------

    input_data = input_data[features]


    # --------------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------------

    fraud_probability = model.predict_proba(
        input_data
    )[0][1]


    # --------------------------------------------------------
    # APPLY SAVED THRESHOLD
    # --------------------------------------------------------

    is_fraud = fraud_probability >= threshold


    probability_percentage = (
        fraud_probability * 100
    )


    # ========================================================
    # RESULT
    # ========================================================

    st.divider()


    if is_fraud:

        # ----------------------------------------------------
        # FRAUD RESULT
        # ----------------------------------------------------

        st.markdown(
            f"""
<div class="result-box">

    <div class="result-title">
        🚨 Potential Fraud Detected
    </div>

    <div class="result-probability">
        {probability_percentage:.2f}%
    </div>

    <div class="result-description">
        Estimated probability of fraudulent activity
    </div>

</div>
""",
            unsafe_allow_html=True
        )

        st.error(
            "This transaction has characteristics that "
            "require additional review."
        )


    else:

        # ----------------------------------------------------
        # NORMAL RESULT
        # ----------------------------------------------------

        st.markdown(
            f"""
<div class="result-box">

    <div class="result-title">
        ✅ Transaction Appears Normal
    </div>

    <div class="result-probability">
        {probability_percentage:.2f}%
    </div>

    <div class="result-description">
        Estimated probability of fraudulent activity
    </div>

</div>
""",
            unsafe_allow_html=True
        )

        st.success(
            "No strong indicators of fraudulent activity "
            "were detected."
        )


    # ========================================================
    # RISK ASSESSMENT
    # ========================================================

    st.markdown(
        '<div class="risk-title">Risk Assessment</div>',
        unsafe_allow_html=True
    )


    st.progress(
        min(fraud_probability, 1.0)
    )


    # --------------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------------

    if probability_percentage < 30:

        st.write("🟢 **Risk Level: Low**")

    elif probability_percentage < 70:

        st.write("🟡 **Risk Level: Moderate**")

    else:

        st.write("🔴 **Risk Level: High**")


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    SecurePay · Credit Card Transaction Security

    <br><br>

    Risk assessment is intended to support transaction review
    and should not be treated as a definitive determination of fraud.

</div>
""", unsafe_allow_html=True)