import streamlit as st
from logic import add, subtract, multiply, divide

def main():
    st.set_page_config(page_title="Simple Streamlit Calculator", page_icon="🧮")
    
    st.title("🧮 Simple Calculator")
    st.markdown("---")

    # Use session state for inputs to allow resetting
    if 'num1' not in st.session_state:
        st.session_state.num1 = 0.0
    if 'num2' not in st.session_state:
        st.session_state.num2 = 0.0
    if 'operation' not in st.session_state:
        st.session_state.operation = "Addition"

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("First Number", value=st.session_state.num1, key="num1_input")
    
    with col2:
        num2 = st.number_input("Second Number", value=st.session_state.num2, key="num2_input")

    operation = st.selectbox(
        "Choose an operation",
        ("Addition", "Subtraction", "Multiplication", "Division"),
        index=("Addition", "Subtraction", "Multiplication", "Division").index(st.session_state.operation),
        key="op_input"
    )

    result = None
    error = None

    if st.button("Calculate"):
        try:
            if operation == "Addition":
                result = add(num1, num2)
            elif operation == "Subtraction":
                result = subtract(num1, num2)
            elif operation == "Multiplication":
                result = multiply(num1, num2)
            elif operation == "Division":
                result = divide(num1, num2)
        except ValueError as e:
            error = str(e)

    if result is not None:
        st.success(f"Result: {result}")
    elif error:
        st.error(error)

    st.markdown("---")
    
    if st.button("Reset"):
        st.session_state.num1 = 0.0
        st.session_state.num2 = 0.0
        st.session_state.operation = "Addition"
        st.rerun()

if __name__ == "__main__":
    main()
