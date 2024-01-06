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

st.text("Explicit indication of data types with :_ suffix:")
text = """
\'b:N\' indicates a nominal type (unordered, categorical data),
'b:O' indicates an ordinal type (rank-ordered data),
'b:Q' indicates a quantitative type (numerical data with meaningful magnitudes), and
'b:T' indicates a temporal type (date/time data)
"""
st.write(text)