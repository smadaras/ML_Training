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


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.altair_chart(c, use_container_width=True)

d = (
   alt.Chart(data)
   .mark_point(filled = True)
   .encode(
      alt.X('production_budget_usd'),
      alt.Y('worldwide_gross_usd')
      )
)
st.altair_chart(d, use_container_width=True)

regression = LinearRegression()
regression.fit(X, y)
st.write(f"y = {regression.coef_[0][0]}*x + {regression.intercept_[0]}")
