import streamlit as st
import sys
import os

# ---------- ADD EXTERNAL PATHS ----------
sys.path.append(os.path.abspath("../model"))
sys.path.append(os.path.abspath("../prompt"))

# ---------- IMPORT YOUR FILES ----------
from model_api import query_model
from prompt_builder import build_prompt, calculate_bmi, bmi_category


# ---------- STREAMLIT UI ----------
st.title("🏋️ AI Personalized 5-Day Workout Planner")

name = st.text_input("Name")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

height = st.number_input("Height (cm)", min_value=0, max_value=250)
weight = st.number_input("Weight (kg)", min_value=0, max_value=200)

goal = st.selectbox("Fitness Goal",["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"])

fitness_level = st.selectbox("Fitness Level", [
    "Beginner",
    "Intermediate",
    "Advanced"
])

equipment = st.multiselect(
    "Available Equipment",
   ["Dumbbells", "Resistance Band", "Yoga Mat", "Skipping Rope",
     "Weight Plates", "Cycling", "Inclined Bench", "Pullups Bar", "No Equipment"]
)

# ---------- GENERATE PLAN ----------
if st.button("Generate 5-Day Plan 💪"):

    prompt, bmi, bmi_status = build_prompt(
        name, gender, height, weight,
        goal, fitness_level, equipment
    )

    st.subheader(f"Your BMI: {bmi:.2f} ({bmi_status})")

    with st.spinner("Creating your personalized workout plan..."):
        result = query_model(prompt)

    st.markdown("## 🗓️ Your 5-Day Workout Plan")
    st.write(result)
