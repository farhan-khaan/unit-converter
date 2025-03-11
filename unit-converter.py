import streamlit as st

# Custom CSS for styling
st.markdown(
    '''
    <style>
    body {
        background-color: #f0f2f6;
        color: #000000;
    }
    .stApp {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
    }
    h1 {
        color: black;
        text-align: center;
    }
    .stbutton {
        background-color: #00b09b;
        color: #ffffff;
        border-radius: 5px;
        padding: 10px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        transition: background-color 0.3s ease;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
    }
    .stbutton:hover {
        background-color: #96c93d;
        transform: scale(1.05);
    }
    .resultsbox {
        background-color: #00b09b;
        color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #000000;
        font-weight: bold;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Convert length, weight, and temperature units easily.")

# Sidebar UI
with st.sidebar:
    st.markdown("<h2>Unit Converter</h2>", unsafe_allow_html=True)
    converter_type = st.selectbox("Converter Type", ["Length", "Weight", "Temperature"])
    value_input = st.number_input("Enter value to convert", value=0.0, min_value=0.0, step=0.1)  # Ensure float type

    col1, col2 = st.columns(2)

    # Unit selection based on conversion type
    if converter_type == "Length":
        with col1:
            from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
        with col2:
            to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    elif converter_type == "Weight":
        with col1:
            from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
        with col2:
            to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
    elif converter_type == "Temperature":
        with col1:
            from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

    convert_button = st.button("💠 Convert 💠")

# Conversion Functions
def convert_length(from_unit, to_unit, value):
    length_units = {
        "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001,
        "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254
    }
    return value * (length_units[from_unit] / length_units[to_unit])

def convert_weight(from_unit, to_unit, value):
    weight_units = {
        "Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001,
        "Pound": 0.453592, "Ounce": 0.0283495
    }
    return value * (weight_units[from_unit] / weight_units[to_unit])

def convert_temperature(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return value * 9/5 + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value  # If same unit, return the original value

# Perform conversion when button is clicked
if convert_button:
    if converter_type == "Length":
        result = convert_length(from_unit, to_unit, value_input)
    elif converter_type == "Weight":
        result = convert_weight(from_unit, to_unit, value_input)
    elif converter_type == "Temperature":
        result = convert_temperature(from_unit, to_unit, value_input)

    # Display result
    st.markdown(f"<div class='resultsbox'>{value_input} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed by <a href="https://github.com/farhan-khaan">Farhan Khan</a></div>', unsafe_allow_html=True)
