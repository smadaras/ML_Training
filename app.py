import streamlit as st
import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression
# from sklearn import datasets
import altair as alt


data = pd.read_csv('cost_revenue_clean.csv')
st.write(data)
X = pd.DataFrame(data, columns=['production_budget_usd'])
y = pd.DataFrame(data, columns=['worldwide_gross_usd'])

st.altair_chart(
   alt.Chart(data)
      .mark_point(filled = True)
      .encode(
         alt.X('production_budget_usd'),
         alt.Y('worldwide_gross_usd')
      )
)

regression = LinearRegression()
regression.fit(X, y)
st.write(f"y = {regression.coef_}*x + {regression.intercept_}")
