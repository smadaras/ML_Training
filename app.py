import pandas as pd
from pandas import DataFrame
import altair as alt
import streamlit as st

movies_2000 = pd.read_csv('cost_revenue_clean.csv')
# print(movies_2000)


st.altair_chart(alt.Chart((movies_2000).mark_circle(size=100).encode(
    x=alt.X('production_budget_usd', title = "Budget in USD"),
    y=alt.Y('worldwide_gross_usd', title = "Gross in USD"),
    tooltip=['teaching', 'citations']))


#st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#        .mark_circle(color='#0068c9', opacity=0.5)
#        .encode(x='x:Q', y='y:Q'))

    
