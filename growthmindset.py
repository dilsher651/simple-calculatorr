import streamlit as st


# Set page config and title
st.set_page_config(page_title="LuckyDS Calculator 🧮", page_icon="🔢")

# Custom CSS styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4287f5;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #e8f0fe;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔢 LuckyDS Calculator")
st.write("Modern calculator for your calculations 💻")

# Input numbers
num1 = st.number_input("First Number", value=0.0)
num2 = st.number_input("Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (^)")
)

# Calculate button
if st.button("CALCULATE"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result}")
    
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result}")
    
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"{num1} × {num2} = {result}")
    
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"{num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero")
    
    elif operation == "Power (^)":
        result = math.pow(num1, num2)
        st.success(f"{num1} ^ {num2} = {result}")

# Digital calculator info
st.markdown("---")
st.write("About LuckyDS Calculator")
st.info("This modern digital calculator helps you perform basic mathematical operations efficiently.")
