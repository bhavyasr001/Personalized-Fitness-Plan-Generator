FitPlan AI – Personalized Fitness & Diet Generator

1. Objective of the Milestone

The objective of this milestone is to develop an AI-powered system that generates personalized workout and diet plans based on user inputs such as age, gender, fitness goal, BMI, and available equipment. The system uses a Large Language Model to generate structured responses that guide users toward achieving their fitness goals.

2. Model Name Used

The project uses the following model from Hugging Face:

Model: mistralai/Mistral-7B-Instruct-v0.1

This model is used to generate customized workout routines and diet suggestions using prompt-based instructions.

3. Prompt Design Explanation

Prompt engineering was used to guide the model to generate structured fitness plans. The prompt includes user inputs and instructs the model to return a detailed plan.

Example Prompt Structure:

User Details:

Age: {age}

Gender: {gender}

Height: {height}

Weight: {weight}

Fitness Goal: {goal}

Equipment Available: {equipment}

Instruction:
"Generate a weekly workout plan and a balanced diet plan for the user based on the above details."

This structured prompt helps the model generate relevant and consistent results.

4. Steps Performed
Step 1: Model Loading

The model was loaded from Hugging Face using the Transformers pipeline.

Example:

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1"
)
Step 2: Prompt Creation

User input from the application interface is combined with a structured prompt template to guide the model in generating personalized outputs.

Step 3: Inference Testing

The prompt is sent to the model, and the model generates the response containing the workout plan and diet recommendations.

Example:

result = generator(prompt, max_length=500)
print(result[0]["generated_text"])
Step 4: Integration with Application

The model output is displayed in the user interface of the FitPlan application developed using Streamlit.

5. Sample Generated Output

Example Output:

Workout Plan:

Monday: Chest and Triceps (Push-ups, Bench Press)

Tuesday: Back and Biceps (Pull-ups, Dumbbell Rows)

Wednesday: Cardio (Running / Cycling)

Thursday: Legs (Squats, Lunges)

Friday: Shoulders (Overhead Press)

Saturday: Core Workout

Sunday: Rest / Light Stretching

Diet Plan:

Breakfast: Oats with fruits and milk

Lunch: Brown rice, grilled chicken, vegetables

Dinner: Paneer/tofu with salad

Snacks: Nuts, yogurt, fruits

6. Hugging Face Space Deployment Link

The project is deployed on Hugging Face Spaces:

Deployment Link:
https://huggingface.co/spaces/your-username/fitplan-ai

7. Conclusion

This milestone demonstrates the use of prompt engineering and large language models to generate personalized health recommendations. The system can be extended further by integrating more health parameters and advanced AI models.
