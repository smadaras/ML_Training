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

st.write(
    """
chartA = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()
"""
)