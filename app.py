import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


movies_2000 = pd.read_csv('cost_revenue_clean.csv')
st.write(movies_2000)
# exit()
c = (
   alt
      .Chart(movies_2000)
      .mark_point()
      .encode(
         alt.X('production_budget_usd'),
         alt.Y('worldwide_gross_usd')
      )
)

st.altair_chart(
   alt.Chart(movies_2000)
      .mark_point()
      .encode(
         alt.X('production_budget_usd'),
         alt.Y('worldwide_gross_usd')
      )
)
