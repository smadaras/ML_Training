import streamlit as st
import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression
import sklearn
import altair as alt


movies_2000 = pd.read_csv('cost_revenue_clean.csv')
st.write(movies_2000)

st.altair_chart(
   alt.Chart(movies_2000)
      .mark_point(filled = True)
      .encode(
         alt.X('production_budget_usd'),
         alt.Y('worldwide_gross_usd')
      )
)

regression = LinearRegression()
regression.fit(X, y)
print(f"y = {regression.coef_}*x + {regression.intercept_}")
