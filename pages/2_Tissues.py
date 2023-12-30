import streamlit as st
import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression
import altair as alt


data = pd.read_csv('lsd_math_score_data.csv')
st.write(data.describe())
time = data[['Time_Delay_in_Minutes']]
LSD = data[['LSD_ppm']]
score = data[['Avg_Math_Test_Score']]

"""
plt.text(x=0, y=-0.5, s='Wagner et al. (1968)', fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.ylim(1,7)
plt.xlim(0,500)

plt.style.use('classic')"""


chartA = ( 
   alt.Chart(data)
   .mark_line(
      color = '#e74c3c', 
      strokeWidth = 3)
   .encode(
      alt.X('Time_Delay_in_Minutes', title = "Time Delay (min)").scale(domain=(0, 500)),
      alt.Y('LSD_ppm', title = "LDS Concentrate (ppm)").scale(domain=(1, 7)))
   .properties(
      title = "Tissue concentration of LSD over time")
)

chartB = alt.Chart().mark_text(
    align="left",
    baseline="bottom",
    fontSize=14,
    fontWeight=600,
    color='coral'
).encode(
    x=alt.value(410),  # pixels from left
    y=alt.value(290),  # pixels from top
    text=alt.value(["Wagner et al. (1968)"])
)

chartSum = chartA.configure_title(
   fontSize = 40) + chartB
st.altair_chart(chartSum, use_container_width=True)

"""regression = LinearRegression()
regression.fit(X, y)
st.write(f"y = {round(regression.coef_[0][0],2)}*x + {round(regression.intercept_[0],2)}")
data['predicted'] = regression.predict(X)
st.write(data)
e = (
   alt.Chart(data)
   .mark_line(color='red', strokeWidth=10)
   .encode(
      alt.X('production_budget_usd'),
      alt.Y('predicted')
   )
)
st.altair_chart(d + e, use_container_width=True)
st.write(f"Quality of Prediction: {round(regression.score(X, y) * 100, 2)}%")"""
