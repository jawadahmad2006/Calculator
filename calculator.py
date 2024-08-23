import streamlit as st
import addition
import subtraction
import multiplication
import division

def main():
    st.title("Python Calculator")

    st.write("Select operation:")
    operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    if st.button("Calculate"):
        if operation == "Add":
            result = addition.add(num1, num2)
            st.write(f"The result is: {result}")

        elif operation == "Subtract":
            result = subtraction.subtract(num1, num2)
            st.write(f"The result is: {result}")

        elif operation == "Multiply":
            result = multiplication.multiply(num1, num2)
            st.write(f"The result is: {result}")

        elif operation == "Divide":
            try:
                result = division.divide(num1, num2)
                st.write(f"The result is: {result}")
            except ValueError as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
