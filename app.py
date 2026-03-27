import streamlit as st
import numpy as np
import pickle

# Page Config
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="wide"
)

# Load model
model = pickle.load(open("CPP.pkl","rb"))

# ---------- Custom CSS ----------
st.markdown("""
<style>

.title {
font-size:45px;
font-weight:700;
text-align:center;
color:#1f77b4;
}

.subtitle {
text-align:center;
font-size:18px;
color:gray;
margin-bottom:20px;
}

.card {
background-color:#f7f9fc;
padding:20px;
border-radius:12px;
box-shadow:0px 2px 8px rgba(0,0,0,0.1);
margin-bottom:15px;
}

.result-success {
background-color:#e6ffe6;
padding:25px;
border-radius:12px;
text-align:center;
font-size:24px;
font-weight:600;
}

.result-danger {
background-color:#ffe6e6;
padding:25px;
border-radius:12px;
text-align:center;
font-size:24px;
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<p class="title">🩺 Diabetes Risk Prediction System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI powered health risk assessment</p>', unsafe_allow_html=True)

st.write("---")

# ---------- Sidebar ----------
st.sidebar.title("📋 About This App")

st.sidebar.info("""
This AI model predicts **Diabetes Risk** based on health indicators.

Fill the patient details and click **Predict Risk**.
""")

st.sidebar.write("### Normal Health Ranges")

st.sidebar.write("""
BMI: **18.5 – 24.9**

HbA1c: **4.0 – 5.6**

Glucose: **70 – 110**
""")

# ---------- Inputs ----------

st.subheader("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    gender = st.selectbox("Gender", ["Female","Male"], index=0)

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=30
    )

    hypertension = st.selectbox(
        "Hypertension",
        ["No","Yes"],
        index=0
    )

    heart_disease = st.selectbox(
        "Heart Disease",
        ["No","Yes"],
        index=0
    )

    st.markdown('</div>', unsafe_allow_html=True)


with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    smoking_history = st.selectbox(
        "Smoking History",
        ["never","former","not current","current","ever","No Info"],
        index=0
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=24.0
    )

    hba1c = st.number_input(
        "HbA1c Level",
        min_value=3.0,
        max_value=15.0,
        value=5.5
    )

    glucose = st.number_input(
        "Blood Glucose Level",
        min_value=50,
        max_value=300,
        value=100
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# ---------- Encoding ----------

gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0

smoking_map = {
    'never':0,
    'former':1,
    'not current':2,
    'current':3,
    'ever':2,
    'No Info':-1
}

smoking_history = smoking_map[smoking_history]

# ---------- Prediction ----------

if st.button("🔍 Predict Diabetes Risk", use_container_width=True):

    input_data = np.array([[

        gender,
        age,
        hypertension,
        heart_disease,
        smoking_history,
        bmi,
        hba1c,
        glucose

    ]])

    prediction = model.predict(input_data)

    st.write("---")

    st.balloons()

    if prediction[0] == 1:

        st.markdown(
        '<div class="result-danger">⚠️ High Risk: Patient likely has Diabetes</div>',
        unsafe_allow_html=True
        )

    else:

        st.markdown(
        '<div class="result-success">✅ Low Risk: Patient likely does NOT have Diabetes</div>',
        unsafe_allow_html=True
        )