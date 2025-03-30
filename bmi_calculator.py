import streamlit as st

# Title
st.title("BMI Calculator")

# Inputs
weight = st.number_input("Enter your weight (in kg):", min_value=1)
height_feet = st.number_input("Enter your height (in feet):", min_value=0.1)

# Convert height from feet to meters
height_meters = height_feet * 0.3048

# Button to calculate BMI
if st.button("Submit"):
    if height_meters > 0:
        bmi = weight / (height_meters ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

        # Display the BMI category
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.error("Height must be greater than 0.")