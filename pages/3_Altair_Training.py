import altair as alt
import streamlit as st

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

st.write(f"Type of alt.Chart(cars): {type(alt.Chart(cars))}")