import streamlit as st
import pandas as pd
# import numpy as np
from sklearn.linear_model import LinearRegression
import altair as alt
from datetime import datetime


data = pd.read_csv('lsd_math_score_data.csv')
st.write(data.describe())
time = data[['Time_Delay_in_Minutes']]
LSD = data[['LSD_ppm']]
score = data[['Avg_Math_Test_Score']]

"""plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.style.use('classic')"""

alt.themes.enable('opaque')
chartA = ( 
   alt.Chart(
      data, 
      title=alt.Title(
         "Tissue concentration of LSD over time",
         fontSize = 30,
         subtitle=["Wagner et al. (1968)"],
         subtitleColor = 'red',
         subtitleFontSize = 20,
         anchor='start',
         orient='bottom',
         offset=20
      )
   ).mark_line(
      color = '#e74c3c', 
      strokeWidth = 3
   ).encode(
      alt.X(
         'Time_Delay_in_Minutes', 
         title = "Time Delay (min)",
         axis=alt.Axis(tickSize = 40, tickColor = 'yellow')
      ).scale(domain=(0, 500)),
      alt.Y(
         'LSD_ppm', 
         title = "LSD Concentrate (ppm)"
         #tickSize = 10
      ).scale(domain=(1, 7))
   )
)

chartSum = chartA
st.altair_chart(
   chartSum, 
   use_container_width=True
)

current_time = datetime.now().strftime("%H:%M:%S")
st.write(f"Current Time = {current_time}")

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
