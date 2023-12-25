import pandas as pd
from pandas import DataFrame
import altair as alt
import streamlit as st

movies_2000 = pd.read_csv('cost_revenue_clean.csv')
st.write(movies_2000)
exit()
st.altair_chart(alt.Chart(movies_2000))
