🏋️ FitPlan AI — Personalized Workout Generator

🎯 Objective of the Milestone
The objective of this milestone is to design and implement an AI-powered system that generates a personalized 5-day workout plan based on the user's fitness profile.

This milestone focuses on:

Integrating a Large Language Model (LLM)

Designing an effective prompt

Testing inference generation

Displaying structured output in Streamlit

Preparing deployment on Hugging Face Spaces


🤖 Model Name Used

Qwen/Qwen2.5-7B-Instruct

Provider: Hugging Face Inference API

This model was selected because:

Instruction-tuned (good for task-based generation)

Generates structured responses

Suitable for fitness plan creation

Works efficiently with prompt engineering


🧠 Prompt Design Explanation

The prompt is carefully engineered to simulate a certified professional fitness trainer.

Prompt includes:

User Profile:

Name

Age

Gender

Height & Weight

BMI + Category

Fitness Goal

Fitness Level

Available Equipment

Instruction Constraints:

The model is instructed to:

Generate a structured 5-day plan

Include exercises with sets & reps

Include rest time

Adjust intensity based on BMI & age

Avoid unsafe exercises for beginners

Maintain professional tone

This ensures consistent and relevant output.

⚙️ Steps Performed
1️⃣ Model Loading

The Hugging Face InferenceClient is used to connect to the LLM:

API token stored securely using environment variables

Model loaded externally in the model folder

2️⃣ Prompt Creation

Prompt is dynamically generated using user input:

BMI calculated using formula

BMI category determined

Equipment list formatted

Personalized instructions embedded

3️⃣ Inference Testing

Steps performed:

Prompt sent to model

Model generated workout plan

Response validated for structure

Displayed in Streamlit interface


🧪 Sample Generated Output
Example User Profile

Age: 21

Goal: Build Muscle

Level: Beginner

Equipment: Dumbbells

Generated Plan (Excerpt)

Your BMI: 18.90 (Normal Weight)
🗓️ Your 5-Day Workout Plan
5-Day Personalized Workout Plan for Bhavya
Note: Since Bhavya is a beginner and has a normal weight, the workout intensity will be moderate. It's important to focus on proper form and gradually increase the weight as she progresses.

Day 1: Upper Body Focus
Warm-Up (5-10 minutes)

Jumping Jacks: 2 minutes
Arm Circles: 30 seconds each direction
Dynamic Stretching: Shoulder rolls and wrist rotations
Dumbbell Bicep Curls

Sets: 3
Reps: 12-15
Rest: 60 seconds
Dumbbell Shoulder Press

Sets: 3
Reps: 12-15
Rest: 60 seconds
Dumbbell Rows

Sets: 3
Reps: 12-15 (each arm)
Rest: 60 seconds
Dumbbell Flyes

Sets: 3
Reps: 12-15
Rest: 60 seconds
Tricep Dips (using a chair)

Sets: 3
Reps: 10-12
Rest: 60 seconds
Cool Down and Stretch (5-10 minutes)
Static Stretching: Focus on arms, shoulders, and back


Day 2: Full Body
Warm-Up (5-10 minutes)

Mountain Climbers: 2 minutes
Leg Swings: 30 seconds each leg
Arm Circles: 30 seconds each direction
Dumbbell Squats

Sets: 3
Reps: 15-20
Rest: 60 seconds
Dumbbell Lunges

Sets: 3
Reps: 12-15 (each leg)
Rest: 60 seconds
Dumbbell Chest Press

Sets: 3
Reps: 12-15
Rest: 60 seconds
Dumbbell Bent Over Rows

Sets: 3
Reps: 12-15
Rest: 60 seconds
Plank (hold with a dumbbell on each side for added resistance)

Sets: 3
Time: 30-45 seconds
Rest: 60 seconds
Cool Down and Stretch (5-10 minutes)
Static Stretching: Focus on legs, back, and core


Day 3: Rest and Recovery
Rest Day
Gentle stretching or light activities like walking or yoga
Focus on proper nutrition and hydration


Day 4: Lower Body Focus
Warm-Up (5-10 minutes)
Leg Swings: 30 seconds each leg
Hip Circles: 30 seconds each direction
Dumbbell Deadlifts

Sets: 3
Reps: 12-15
Rest: 60 seconds
Dumbbell Sumo Squats

Sets: 3
Reps: 15-20
Rest: 60 seconds
Dumbbell Calf Raises

Sets: 3
Reps: 15-20
Rest: 60 seconds
Dumbbell Step-Ups

Sets: 3
Reps: 12-15 (each leg)
Rest: 60 seconds
Cool Down and Stretch (5-10 minutes)
Static Stretching: Focus on legs and glutes


Day 5: Core and Upper Body
Warm-Up (5-10 minutes)
Arm Swings: 30 seconds each direction
Leg Swings: 30 seconds each leg
Dumbbell Russian Twists

Sets: 3
Reps: 15-20 (each side)
Rest: 60 seconds
Dumbbell Plank with Leg Lifts

Sets: 3
Time: 30-45 seconds
Rest: 60 seconds
Dumbbell Push-Ups

Sets: 3
Reps: 10-12
Rest: 60 seconds
Dumbbell Rows (standing with a dumbbell in each hand)

Sets: 3
Reps: 12-15 (each arm)
Rest: 60 seconds
Cool Down and Stretch (5-10 minutes)
Static Stretching: Focus on core, chest, and arms

General Tips:
Hydration: Drink plenty of water throughout the day.
Nutrition: Focus on balanced meals with lean proteins, complex carbohydrates, and healthy fats.
Consistency: Stick to the plan and gradually increase the weight as you get stronger.
Form: Prioritize proper form over the weight used. Incorrect form can lead to injuries.
Feel free to adjust the weights and reps based on how your body feels. If you experience any discomfort or pain, consult a healthcare professional.

🌐 Hugging Face Space Deployment Link

👉 Deployed app link here:

[https://huggingface.co/spaces/srbhavya01/Module_2]
