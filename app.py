from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load dataset
df = pd.read_csv("gym_members_exercise_tracking_synthetic_data.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    age = int(request.form["age"])
    gender = request.form["gender"]
    weight = float(request.form["weight"])
    height = float(request.form["height"])
    workout_type = request.form["workout_type"]
    duration = float(request.form["duration"])

    # Calculate BMI
    bmi = round(weight / (height ** 2), 2)

    # Calorie burn prediction (example: based on workout type & duration)
    calorie_burn_rate = {"Cardio": 8, "Strength": 6, "Yoga": 3}
    calories_burned = round(calorie_burn_rate.get(workout_type, 5) * duration * weight, 2)

    # Determine health status
    health_status = "Healthy" if 18.5 <= bmi <= 24.9 else "Unhealthy"

    return render_template(
        "result.html",
        age=age,
        gender=gender,
        weight=weight,
        height=height,
        bmi=bmi,
        calories_burned=calories_burned,
        health_status=health_status,
    )

if __name__ == "__main__":
    app.run(debug=True)
