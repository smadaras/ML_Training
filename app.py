import streamlit as st
import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression
import altair as alt


data = pd.read_csv('cost_revenue_clean.csv')
X = pd.DataFrame(data, columns=['production_budget_usd'])
y = pd.DataFrame(data, columns=['worldwide_gross_usd'])

d = (
   alt.Chart(data)
   .mark_point(filled = True)
   .encode(
      alt.X('production_budget_usd'),
      alt.Y('worldwide_gross_usd')
      )
)

regression = LinearRegression()
regression.fit(X, y)
st.write(f"y = {round(regression.coef_[0][0],2)}*x + {round(regression.intercept_[0],2)}")
data['predicted'] = regression.predict(X)
st.write(data)
e = (
   alt.Chart(data)
   .mark_line(color='red', width=10)
   .encode(
      alt.X('production_budget_usd'),
      alt.Y('predicted')
   )
)
st.altair_chart(d + e, use_container_width=True)
st.write(f"Quality of Prediction: {round(regression.score(X, y) * 100, 2)}%")
