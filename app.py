import streamlit as st
import pandas as pd
import numpy as np
import joblib


model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Placements Eligibility Prediction",page_icon="🎓", layout = "centered")

st.title("🎓 Placement Eligibility Predictor")

st.write("Predict whether a student is eligible for placements based on CGPA, Aptitude Score and Attendance.")
st.divider()


cgpa = st.number_input("CGPA", min_value = 0.0, max_value = 10.0, value = 7.5, step = 0.1)
aptitude_score = st.number_input("Aptitude_Score", min_value = 0, max_value = 100, value = 70, step = 1)
attendance = st.number_input("Attendance (%)", min_value = 0, max_value = 100, value = 80, step = 1)

if st.button("Predict Placement Eligibility"):
    input_data = pd.DataFrame([[cgpa, aptitude_score, attendance]], columns=['CGPA', 'Aptitude_Score', 'Attendance'])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1] 

    st.divider()
    if prediction[0] == 1:
        st.success("✅ Student is Eligible for Placement")
    else:
        st.error("❌ Student is Not Eligible for Placement")

    st.info(f"Eligibility Probability:" f"{probability:.2f}%")
