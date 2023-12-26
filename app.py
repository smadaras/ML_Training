import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
# from sklearn import datasets
import altair as alt


data = pd.read_csv('cost_revenue_clean.csv')
st.write(data)
X = pd.DataFrame(data, columns=['production_budget_usd'])
Y = pd.DataFrame(data, columns=['worldwide_gross_usd'])

d = (
   alt.Chart(data)
   .mark_point(filled = True)
   .encode(
      #alt.X('production_budget_usd'),
      #alt.Y('worldwide_gross_usd')
      x = X,
      y = Y
      )
)
st.altair_chart(d, use_container_width=True)

regression = LinearRegression()
regression.fit(X, y)
st.write(f"y = {regression.coef_[0][0]}*x + {regression.intercept_[0]}")
# plt.plot(X, regression.predict(X), color='red', linewidth=3)

e = (
   alt.Chart(data)
   .mark_line()
   .encode(
      alt.X(X),
      alt.Y(regression.predict(X))
   )
)
st.altair_chart(e, use_container_width=True)
