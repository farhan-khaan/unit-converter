# unit converter in python 
# by using google unit converter api bu using python and streamlit

import streamlit as st

st.markdown (
    '''
<style>
body {
    background-color: #f0f2f6;
    color: #000000;
}
.stApp {
    background-color: #f0f2f6;
    linear-gradient(to right, #00b09b, #96c93d);
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
}
h1 {
    color: #000000;
    text-align: center;
}
.stbutton {
    background-color: #00b09b;
    color: #000000;
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
    background-color: #00b09b;
    transform: scale(1.05);
    color: #000000;
    linear-gradient(to right, #00b09b, #96c93d);
    border: 2px solid #000000;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
}
.stresultsbox {
    background-color: #00b09b;
    color: #000000;
    border-radius: 5px;
    padding: 10px;
    border: none;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
    font-size: 16px;
    font-weight: bold;
    text-transform: uppercase;
    transition: background-color 0.3s ease;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
    text-align: center;
    margin: 20px;
    width: 50%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
    font-size: 16px;
    font-weight: bold;
    text-transform: uppercase;
    transition: background-color 0.3s ease;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
    text-align: center;
    margin: 20px;
    width: 50%;
    height: 50%;
}
.stresultsbox:hover {
    background-color: #00b09b;
    transform: scale(1.05);
    color: #000000;
    linear-gradient(to right, #00b09b, #96c93d);
    border: 2px solid #000000;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
    text-align: center;
    margin: 20px;
    width: 50%;
    height: 50%;
}
#footer {
    text-align: center;
    margin: 20px;
    width: 50%;
    height: 50%;
    background-color: #00b09b;
    color: #000000;
    border-radius: 5px;
    padding: 10px;
    border: none;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);
}
#footer:hover {
    background-color: #00b09b;
    transform: scale(1.05);
    color: #000000;
    linear-gradient(to right, #00b09b, #96c93d);
}
</style>
    ''',
    unsafe_allow_html = True
)

# Title of the app
st.markdown("<h1 style='text-align: center;'>Unit Converter by using python and streamlit</h1>", unsafe_allow_html=True)
st.write(" You can convert units of length, weight, temperature, and more.")

# side bar for the user
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Unit Converter by using python and streamlit</h1>", unsafe_allow_html=True)
    st.write(" You can convert units of length, weight, temperature, and more.")
    converter_type = st.selectbox("Converter Type", ["Length", "Weight", "Temperature"])
    value_input = st.number_input("Enter the value to convert", value=0, min_value=0.0, step=0.1)
    col1, col2 = st.columns(2)

    if converter_type == "Length":
        with col1:
            from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"])
        with col2:
            to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"])
        
    elif converter_type == "Weight":
        with col1:
            from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Microgram", "Pound", "Ounce"])
        with col2:
            to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Microgram", "Pound", "Ounce"])
        
    elif converter_type == "Temperature":
        with col1:
            from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        
    convert_button = st.button("Convert")

    # converted function
def convert_unit(from_unit, to_unit, value_input):
    length_units = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Micrometer": 0.000001, "Nanometer": 0.000000001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254, "Nautical Mile": 1852}
    return value_input * length_units[from_unit] / length_units[to_unit]

def convert_weight(from_unit, to_unit, value_input):
    weight_units = {"Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001, "Microgram": 0.000000001, "Pound": 0.453592, "Ounce": 0.0283495}
    return value_input * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(from_unit, to_unit, value_input):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return value_input * 9/5 + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value_input + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value_input - 32) * 5/9
    if to_unit == "Celsius" and from_unit == "Fahrenheit":
        return (value_input - 32) * 5/9
    if to_unit == "Celsius" and from_unit == "Kelvin":
        return value_input - 273.15
    if to_unit == "Kelvin" and from_unit == "Celsius":
        return value_input + 273.15 
    if to_unit == "Kelvin" and from_unit == "Fahrenheit":
        return (value_input - 32) * 5/9 + 273.15
    if to_unit == "Fahrenheit" and from_unit == "Kelvin":
        return (value_input - 273.15) * 9/5 + 32
    if to_unit == "Fahrenheit" and from_unit == "Celsius":
        return value_input * 9/5 + 32
    if to_unit == "Celsius" and from_unit == "Kelvin":
        return value_input - 273.15
    if to_unit == "Kelvin" and from_unit == "Celsius":
        return value_input + 273.15
    if to_unit == "Kelvin" and from_unit == "Fahrenheit":
        return (value_input - 32) * 5/9 + 273.15
    if to_unit == "Fahrenheit" and from_unit == "Kelvin":
        return (value_input - 273.15) * 9/5 + 32
    
    return value_input 

st.button("💠Convert💠");

if convert_button:
    if converter_type == "Length":
        result = convert_unit(from_unit, to_unit, value_input)
    elif converter_type == "Weight":
        result = convert_weight(from_unit, to_unit, value_input)
    elif converter_type == "Temperature":
        result = convert_temperature(from_unit, to_unit, value_input)

    st.markdown(f"<div class=\"resultsbox\">{value_input} {from_unit} is equal to {result} {to_unit}</div>", unsafe_allow_html=True)
st.markdown(f"<div class=\"footer\">Developed by <a href=\"https://github.com/farhan-khaan\">Farhan Khan</a></div>", unsafe_allow_html=True)
