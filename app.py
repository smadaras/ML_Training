"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)
"""


import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


movies_2000 = pd.read_csv('cost_revenue_clean.csv')
st.write(movies_2000)
# exit()
c = (
   alt.Chart(movies_2000)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)
# st.altair_chart(alt.Chart(movies_2000))
