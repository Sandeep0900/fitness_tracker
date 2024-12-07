import streamlit as st
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

# Remove app.run() from the original file
# Create a Streamlit-specific function to handle the form
def main():
    st.title("Fitness tracking Test")
    
    # Collect input using Streamlit widgets
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    workout_type = st.selectbox("Workout Type", ["Cardio", "Strength", "Yoga"])
    duration = st.number_input("Duration (hours)", min_value=0.1, max_value=5.0, value=1.0)

    # Calculate BMI
    bmi = round(weight / (height ** 2), 2)

    # Calorie burn prediction
    calorie_burn_rate = {"Cardio": 8, "Strength": 6, "Yoga": 3}
    calories_burned = round(calorie_burn_rate.get(workout_type, 5) * duration * weight, 2)

    # Determine health status
    health_status = "Healthy" if 18.5 <= bmi <= 24.9 else "Unhealthy"

    # Display results
    if st.button("Analyze"):
        st.write("### Analysis Results")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Weight:** {weight} kg")
        st.write(f"**Height:** {height} m")
        st.write(f"**BMI:** {bmi}")
        st.write(f"**Calories Burned:** {calories_burned}")
        st.write(f"**Health Status:** {health_status}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
