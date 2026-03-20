def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "#3498db"
    elif bmi < 25:
        return "Normal Weight", "#2ecc71"
    elif bmi < 30:
        return "Overweight", "#f1c40f"
    else:
        return "Obese", "#e74c3c"


def build_prompt(name, gender, age, height, weight, goal, fitness_level, equipment):

    bmi = calculate_bmi(weight, height)
    bmi_status, status_color = bmi_category(bmi)

    equipment_list = ", ".join(equipment) if equipment else "No Equipment"

    prompt = f"""
Create a 5 day workout plan.

User:
Age: {age}
Gender: {gender}
BMI: {bmi:.2f}
Goal: {goal}
Fitness Level: {fitness_level}
Equipment: {equipment_list}

Format:
Exercise | Sets | Reps | Rest
"""

    return prompt, bmi, bmi_status, status_color
