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

chartA = ( 
   alt.Chart(
      data, 
      title=alt.Title(
         "Tissue concentration of LSD over time",
         fontSize = 30,
         subtitle=["Wagner et al. (1968)"],
         subtitleColor = 'grey',
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
         axis = alt.Axis(tickCount = 10) # tickSize, tickWidth, tickColor are not implemented
      ).scale(domain=(0, 500)),
      alt.Y(
         'LSD_ppm', 
         title = "LSD Concentrate (ppm)"
      ).scale(domain=(1, 7))
   )
)

chartSum = chartA

alt.themes.enable('none')
st.altair_chart(
   chartSum, 
   use_container_width = True
)

regr = LinearRegression()
regr.fit(LSD, score)
st.write('Theta1 : ', regr.coef_[0][0])
st.write('Intercept: ', regr.intercept_[0])
st.write('R-Square: ', regr.score(LSD, score))
predicted_score = regr.predict(LSD)
data['predicted_score'] = regr.predict(LSD)
# score = data[['Avg_Math_Test_Score']]
st.write(data)
# st.write('Predicted Score: ', predicted_score)

current_time = datetime.now().strftime("%H:%M:%S")
st.write(f"Current Time = {current_time}")

chartB = (
   alt.Chart(
      data, 
      title = alt.Title(
         "Arithmetic vs LSD-25",
         fontSize = 17)
   ).mark_point(
      color='blue', 
      filled=True # pointsize?
   ).encode(
      alt.X(
         'LSD_ppm',
         title = 'Tissue LSD ppm' # fontsize?
         ).scale(domain=(1,6.5)),
      alt.Y(
         'Avg_Math_Test_Score',
         title = 'Performance Score' # fontsize?
         ).scale(domain=(25,85))
   )
)

chartC = (
   alt.Chart(data)
   .mark_line(color='red', strokeWidth=3)
   .encode(
      alt.X('LSD_ppm'),
      alt.Y('predicted_score')
   )
)

chartSum = chartB + chartC


alt.themes.enable('fivethirtyeight')
st.altair_chart(chartSum, use_container_width=True)
st.write(f"Quality of Prediction: {round(regr.score(LSD, score) * 100, 2)}%")
