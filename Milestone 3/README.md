# FitPlan AI – Personalized Fitness Planner

## 1. Objective of the Milestone

The objective of this milestone is to develop an AI-powered fitness planning application that generates personalized workout routines based on user details such as age, gender, BMI, fitness goal, fitness level, and available equipment.

The system integrates prompt engineering with a Large Language Model to generate structured workout plans. Additionally, the application provides secure user authentication and email-based OTP verification.

---

## 2. Model Name Used

The project uses the **Groq API** to access a Large Language Model.

**Model Used:**
llama-3.1-8b-instant

This model generates customized workout plans based on structured prompts and user fitness information.

---

## 3. Prompt Design Explanation

Prompt engineering is used to guide the AI model to generate a structured workout plan.

The prompt contains the following user information:

* Name
* Age
* Gender
* BMI
* Fitness goal
* Fitness level
* Available equipment

The prompt also contains strict formatting rules to ensure consistent output.

Formatting Rules:

1. Label workout days as **Day 1, Day 2, Day 3, Day 4, Day 5**
2. Each exercise must follow this format:

Exercise Name | Sets | Reps | Rest

Example:

Dumbbell Bench Press | 3 | 10-12 | 60s

3. **Day 3 must always be a Rest Day**
4. The model should generate only the workout plan without any introduction or extra explanation.

This structured prompt ensures the output remains consistent and easy to display in the application.

---

## 4. Steps Performed

### Step 1: Database Initialization

The application uses **SQLite** to store user information.

A `users` table is created to store:

* id
* name
* email
* password_hash
* created_at
* updated_at

---

### Step 2: User Authentication

The system provides secure authentication features including:

• Password hashing using `werkzeug.security`
• JWT token generation for secure sessions
• OTP verification through email

Passwords are stored securely as hashed values.

---

### Step 3: OTP Email Verification

When a user registers or logs in, a **6-digit OTP** is generated and sent to the user's email using **SendGrid API**.

Example email message:

Your OTP is: 482915

This ensures secure verification of user accounts.

---

### Step 4: BMI Calculation

The system calculates the Body Mass Index using:

BMI = Weight / Height²

Users are categorized as:

* Underweight
* Normal Weight
* Overweight
* Obese

---

### Step 5: Prompt Creation

User fitness details are converted into a structured prompt using the `build_prompt()` function.

Example:

```python
prompt, bmi, bmi_status, status_color = build_prompt(
    name, gender, age, height, weight, goal, fitness_level, equipment
)
```

---

### Step 6: Model Inference

The prompt is sent to the Groq API which runs the **Llama 3.1 model** to generate a workout plan.

Example:

```python
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "You are a professional fitness trainer and nutritionist."},
        {"role": "user", "content": prompt}
    ]
)
```

---

### Step 7: Displaying Results

The generated workout plan is displayed to the user through the **Streamlit web interface**.

---

## 5. Sample Generated Output

Example AI Output:

Day 1:
Push Ups | 3 | 12-15 | 60s
Dumbbell Bench Press | 3 | 10-12 | 60s
Tricep Dips | 3 | 12 | 45s

Day 2:
Pull Ups | 3 | 8-10 | 90s
Dumbbell Rows | 3 | 10-12 | 60s
Bicep Curls | 3 | 12 | 45s

Day 3:
Rest Day

Day 4:
Squats | 4 | 10-12 | 90s
Lunges | 3 | 12 | 60s

Day 5:
Shoulder Press | 3 | 10 | 60s
Lateral Raises | 3 | 12 | 45s

---

## 6. Hugging Face Space Deployment Link

Project Deployment Link:

[https://huggingface.co/spaces/Infoysprojectwork/AI-Fitness-Plan-Generator]

---

## 7. Conclusion

FitPlan AI demonstrates how Large Language Models can be integrated with prompt engineering, secure authentication, and user data to generate personalized fitness plans. The system provides an intelligent AI-based fitness assistant that adapts to individual user goals and equipment availability.
