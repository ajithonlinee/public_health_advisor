import streamlit as st
import numpy as np
import pickle
MODEL_URL = "https://drive.google.com/uc?export=download&id=1h7VsiZlMLxW8CaLsru-JzNBxHN7D-9Js"
if not os.path.exists("health_model.pkl"):
    r = requests.get(MODEL_URL)
    with open("health_model.pkl", "wb") as f:
        f.write(r.content)
model = pickle.load(open("health_model.pkl", "rb"))
st.set_page_config(page_title="Personal Health Advisor", page_icon="🩺")
st.title("🩺 Personal Health Advisor")
st.write("Predict your risk of diabetes using your health information")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 1, 100)
hypertension = st.selectbox("Do you have hypertension?", ["No", "Yes"])
heart_disease = st.selectbox("Do you have heart disease?", ["No", "Yes"])
smoking_history = st.selectbox("Smoking History", ["never", "former", "current", "not current", "ever", "No Info"])
bmi = st.slider("BMI (Body Mass Index)", 10.0, 50.0)
hba1c = st.slider("HbA1c level", 3.0, 9.0)
glucose = st.slider("Blood Glucose Level", 50, 300)
gender_dict = {"Male": 1, "Female": 0, "Other": 2}
smoking_dict = {'never': 4, 'former': 1, 'current': 0, 'not current': 2, 'ever': 3, 'No Info': 5}
gender = gender_dict[gender]
smoking = smoking_dict[smoking_history]
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
if st.button("Check My Diabetes Risk"):
    input_data = np.array([[gender, age, hypertension, heart_disease, smoking, bmi, hba1c, glucose]])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ You are at risk of diabetes. Please consult a doctor.")
    else:
        st.success("✅ You are not currently at risk of diabetes.")
