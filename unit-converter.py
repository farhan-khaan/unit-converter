import streamlit as st

# Custom CSS for better styling and responsiveness
st.markdown(
    """
    <style>
    /* Background & layout */
    .stApp {
        background-color: #f9f9f9;
        padding: 20px;
    }
    
    /* Header - Change h1 to Black */
    h1 {
        color: black !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }

    h2 {
        color: #333;
        text-align: center;
    }
    h3 {
        color: black !important;
        text-align: center;
    }

    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #00b09b;
        color: white;
        border-radius: 10px;
        padding: 15px;
    }

    /* Buttons */
    .stbutton {
        background-color: #00b09b;
        color: white;
        border-radius: 5px;
        padding: 10px;
        border: none;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        transition: background-color 0.3s ease, transform 0.2s ease;
        width: 100%;
    }

    .stbutton:hover {
        background-color: #96c93d;
        transform: scale(1.05);
    }

    /* Result Box */
    .resultsbox {
        background-color: #00b09b;
        color: white;
        border-radius: 10px;
        padding: 20px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
/* Error Message Styling */
    .error-message {
        background-color: #ffcccc;  /* Light Red Background */
        color: #b30000;  /* Dark Red Text */
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        margin-top: 10px;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 20px;
        color: #333;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>⚖️ Unit Converter</h1>", unsafe_allow_html=True)
st.write("<h3>Easily convert Length, Weight, and Temperature units.</h3>", unsafe_allow_html=True)

# Sidebar UI
with st.sidebar:
    st.markdown("<h2>⚙️ Choose Conversion</h2>", unsafe_allow_html=True)
    converter_type = st.selectbox("Converter Type", ["Length", "Weight", "Temperature"])
    value_input = st.number_input("Enter value to convert", value=0.0, min_value=0.0, step=0.1, format="%.2f")

    col1, col2 = st.columns(2)

    # Unit selection based on conversion type
    if converter_type == "Length":
        units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    elif converter_type == "Weight":
        units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    else:
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    with col1:
        from_unit = st.selectbox("From Unit", units)
    with col2:
        to_unit = st.selectbox("To Unit", units)

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
    return value  # If same unit, return original value

# Perform conversion when button is clicked
if convert_button:
    if from_unit == to_unit:
        st.markdown(
            "<div class='error-message'>⚠️ Please select different units for conversion.</div>", 
            unsafe_allow_html=True
        )
    else:
        if converter_type == "Length":
            result = convert_length(from_unit, to_unit, value_input)
        elif converter_type == "Weight":
            result = convert_weight(from_unit, to_unit, value_input)
        elif converter_type == "Temperature":
            result = convert_temperature(from_unit, to_unit, value_input)

        # Display result in 00.00 format
        st.markdown(f"<div class='resultsbox'>{value_input:.2f} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed by <a href="https://github.com/farhan-khaan">Farhan Khan</a></div>', unsafe_allow_html=True)
