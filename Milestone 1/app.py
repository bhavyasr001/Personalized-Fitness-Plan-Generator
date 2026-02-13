import streamlit as st

st.set_page_config(page_title="FitPlan AI - BMI Calculator", page_icon="💪")

st.title("💪 FitPlan AI - Fitness Profile & BMI Calculator")

st.write("Fill in your details to calculate your BMI and fitness category.")

# -------------------------
# 1. Personal Information
# -------------------------

name = st.text_input("Enter Your Name *")

height_cm = st.number_input("Enter Height (in centimeters) *", min_value=0.0, format="%.2f")
weight_kg = st.number_input("Enter Weight (in kilograms) *", min_value=0.0, format="%.2f")

# -------------------------
# 2. Fitness Details
# -------------------------

st.subheader("Fitness Details")

goal = st.selectbox(
    "Select Your Fitness Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

equipment = st.multiselect(
    "Available Equipment (Select multiple if available)",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment"]
)

fitness_level = st.radio(
    "Select Your Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

# -------------------------
# BMI Calculation Function
# -------------------------

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# -------------------------
# Submit Button
# -------------------------

if st.button("Calculate BMI"):
    
    # Validation
    if not name or height_cm <= 0 or weight_kg <= 0:
        st.error("⚠ Please fill all required fields with valid values!")
    else:
        bmi = calculate_bmi(weight_kg, height_cm)
        category = bmi_category(bmi)

        st.success("✅ Calculation Successful!")

        st.write(f"### 👤 Name: {name}")
        st.write(f"### 📊 Your BMI: {bmi}")
        st.write(f"### 🏷 BMI Category: {category}")

        st.write("---")
        st.write("### 🏋 Fitness Summary")
        st.write(f"**Goal:** {goal}")
        st.write(f"**Fitness Level:** {fitness_level}")
        st.write(f"**Equipment Available:** {', '.join(equipment) if equipment else 'None selected'}")
