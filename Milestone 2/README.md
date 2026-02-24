🎯 Objective of the Milestone

The objective of this milestone is to develop an AI-powered personalized fitness planning system that generates a structured 5-day workout plan based on user inputs such as height, weight, gender, fitness level, goal, and available equipment.

This milestone demonstrates:

Integration of a Large Language Model (LLM)

Prompt engineering for personalized outputs

Health-based customization using BMI

Deployment-ready application using Streamlit

The system acts as a virtual fitness trainer that produces safe, structured, and goal-oriented workout routines.

🤖 Model Used

Model Name: Mistral AI — Mistral-7B-Instruct-v0.2

Platform: Hugging Face Inference API

Access Method: huggingface_hub InferenceClient

The model is an instruction-tuned LLM capable of generating structured fitness plans based on prompts.

🧠 Prompt Design Explanation

The prompt was carefully engineered to guide the model to produce structured and safe workout plans.

Key prompt features:

Includes detailed user profile

Uses BMI calculation for personalization

Specifies formatting rules (Day 1–Day 5)

Requests exercises with sets, reps, and rest

Adjusts intensity based on fitness level

Avoids unsafe exercises for beginners

Example prompt components:

Personal details

Fitness goal

Equipment availability

Safety instructions

Output formatting requirements

This ensures consistent and high-quality responses.

⚙️ Steps Performed
1️⃣ Model Loading

Loaded Mistral-7B-Instruct-v0.2 via Hugging Face InferenceClient

Authentication using HF_TOKEN environment variable

2️⃣ Prompt Creation

Calculated BMI using height and weight

Determined BMI category

Constructed personalized prompt using user inputs

3️⃣ Inference Testing

Sent prompt to model

Generated structured 5-day workout plan

Displayed output in Streamlit interface

🧪 Sample Generated Output
🏋️ Example User Profile

Name: Rahul

Gender: Male

Height: 175 cm

Weight: 78 kg

BMI: 25.47 (Overweight)

Goal: Weight Loss

Fitness Level: Beginner

Equipment: Dumbbells

📅 Sample Plan (Excerpt)

Day 1 — Full Body Fat Burn

Jump Rope

Sets: 3

Duration: 1 min

Rest: 30 sec

Dumbbell Squats

Sets: 3

Reps: 12

Rest: 60 sec

Push-ups

Sets: 3

Reps: 10

Rest: 60 sec

The model generated structured plans for all five days with progressive intensity.

🚀 Hugging Face Space Deployment

🔗 Deployment Link: https://huggingface.co/spaces/srbhavya01/Module_2

🖥️ Technologies Used

Python

Streamlit

Hugging Face Hub

Large Language Model (LLM)

Docker (for containerization)

📌 Conclusion

This milestone successfully demonstrates the application of generative AI in personalized fitness planning. The system can be extended with diet plans, progress tracking, and mobile deployment in future work.
