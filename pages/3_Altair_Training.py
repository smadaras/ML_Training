import altair as alt
import streamlit as st
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")
st.write(f"Current Time = {current_time}")

# load a simple dataset as a pandas DataFrame
from vega_datasets import data
cars = data.cars()

chartA = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

st.altair_chart(
    chartA,
    use_container_width = True
)

code = """
alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()
"""
st.code(code,language='python')

st.write(f"Type of alt.Chart() and all its derivatives: {type(alt.Chart(cars))}")