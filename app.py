import pandas as pd
from pandas import DataFrame
import altair as alt
import streamlit as st

movies_2000 = pd.read_csv('cost_revenue_clean.csv')
# print(movies_2000)


st.altair_chart(
    alt.Chart(
        (movies_2000).mark_circle(size=100).encode(
            x=alt.X('production_budget_usd', title = "Budget in USD"),
            y=alt.Y('worldwide_gross_usd', title = "Gross in USD"),
            tooltip=['teaching', 'citations'])
    )
)
