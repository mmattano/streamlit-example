from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import datetime
from datetime import date

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
"""

st.title('Welcome to the /"Matthias loves and misses Holda very much/" app!')

st.write('Progress of the external stay')

def get_difference(date1, date2):
    delta = date2 - date1
    return delta.days

d1 = datetime(2023, 2, 12)
d_current = datetime.now()
d2 = datetime(2023, 5, 13)
days_total = get_difference(d1, d2)
days_past = get_difference(d1, d_current)
ratio = days_past / days_total
st.progress(ratio)