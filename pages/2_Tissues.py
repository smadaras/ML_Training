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

"""plt.title('Tissue concentration of LSD over time', fontsize=17)
plt.xlabel('Time in Minutes', fontsize=14)
plt.ylabel('Tissue LSD ppm', fontsize=14)
plt.text(x=0, y=-0.5, s='Wagner et al. (1968)', fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.ylim(1,7)
plt.xlim(0,500)

plt.style.use('classic')

alt.Chart(
   iowa,
   title=alt.Title(
       "Iowa's green energy boom",
       subtitle="A growing share of the state's energy has come from renewable sources"
   )
).mark_area().encode(
    x="year:T",
    y=alt.Y("net_generation:Q").stack("normalize"),
    color="source:N"
)"""


chartA = ( 
   alt.Chart(
      data, 
      title = "Tissue concentration of LSD over time"
   )
   .mark_line(color='#e74c3c', strokeWidth=3)
   .encode(
      alt.X('Time_Delay_in_Minutes'),
      alt.Y('LSD_ppm')
   )
   .configure_axis(
      # labelFontSize=40,
      titleFontSize=40
   )
)
st.altair_chart(chartA, use_container_width=True)

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
