import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    weight = st.number_input("Enter your weight (in kg)")
    height = st.number_input("Enter your height (in meters)")

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"Classification: {classify_bmi(bmi)}")

if __name__ == "__main__":
    main()