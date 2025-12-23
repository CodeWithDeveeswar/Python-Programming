# Terminal command: python -m streamlit run Streamlit/simple_calculator.py

import streamlit as st

st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    if operation == "Subtract":
        result = num1 - num2
    if operation == "Multiply":
        result = num1 * num2
    if operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    st.success(f"Result: {result}")