import streamlit as st
import joblib
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Hospital Cost Prediction System",
    page_icon="🏥",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS FOR PROFESSIONAL LOOK
# --------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
    }
    .big-font {
        font-size: 22px;
        font-weight: 600;
    }
    .result-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.08);
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("<h1 style='text-align:center;'>🏥 Hospital Cost Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI-powered estimation of annual medical expenses</p>", unsafe_allow_html=True)

st.divider()

# --------------------------------------------------
# LOAD MODELS
# --------------------------------------------------
models = {
    "Linear Regression": joblib.load("linear_regression_model.joblib"),
    "Ridge Regression": joblib.load("ridge_regression_model.joblib"),
    "Lasso Regression": joblib.load("lasso_regression_model.joblib"),
    "ElasticNet Regression": joblib.load("elasticnet_model.joblib")
}

model_info = {
    "Linear Regression": "Simple baseline model",
    "Ridge Regression": "Handles multicollinearity",
    "Lasso Regression": "Performs feature selection",
    "ElasticNet Regression": "Best balance of Ridge & Lasso"
}

# --------------------------------------------------
# MODEL SELECTION
# --------------------------------------------------
st.subheader("🧠 Model Selection")

col1, col2 = st.columns([2, 1])
with col1:
    selected_model_name = st.selectbox(
        "Choose a prediction model",
        list(models.keys())
    )
with col2:
    st.info(model_info[selected_model_name])

selected_model = models[selected_model_name]

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
st.subheader("📋 Patient & Insurance Details")

col1, col2 = st.columns(2)

with col1:
    monthly_premium = st.number_input("Monthly Premium ($)", 0.0, step=10.0)
    total_claims_paid = st.number_input("Total Claims Paid ($)", 0.0, step=100.0)
    risk_score = st.slider("Risk Score", 0.0, 1.0, 0.5, 0.01)

with col2:
    annual_premium = st.number_input("Annual Premium ($)", 0.0, step=50.0)
    avg_claim_amount = st.number_input("Average Claim Amount ($)", 0.0, step=50.0)
    chronic_count = st.slider("Chronic Conditions Count", 0, 10, 1)

st.divider()

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------
if st.button("🔮 Predict Annual Medical Cost", use_container_width=True):
    input_data = np.array([[
        monthly_premium,
        annual_premium,
        total_claims_paid,
        avg_claim_amount,
        risk_score,
        chronic_count
    ]])

    prediction = selected_model.predict(input_data)[0]

    st.markdown(f"""
    <div class="result-box">
        <p class="big-font">Estimated Annual Medical Cost</p>
        <h2 style="color:#2E86C1;">${prediction:,.2f}</h2>
        <p><b>Model Used:</b> {selected_model_name}</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;font-size:12px;'>Developed using Machine Learning & Streamlit</p>",
    unsafe_allow_html=True
)
