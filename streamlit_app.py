from collections import namedtuple
import streamlit as st
from datetime import datetime
from stolen_from_extras import rain


st.title('Welcome to the "Matthias loves and misses Holda very much" app!')

st.write('Progress of the external stay')


def get_difference(date1, date2):
    delta = date2 - date1
    return delta.days


d1 = datetime(2023, 2, 12)
d_current = datetime.now()
d2 = datetime(2023, 5, 13)
days_total = get_difference(d1, d2)
days_past = get_difference(d1, d_current)
days_to_go = get_difference(d_current, d2)
ratio = days_past / days_total

st.progress(ratio)

st.write('Days to go: ', days_to_go)

if ratio < 0.1:
    st.write('Settling in')
    rain(
        emoji="😮‍💨",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 0.1 and ratio < 0.2:
    st.write('Still a while to go')
    rain(
        emoji="😢",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 0.2 and ratio < 0.3:
    st.write('Time is passing')
    rain(
        emoji="😐",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 0.3 and ratio < 0.45:
    st.write('Still a while to go')
    rain(
        emoji="😐",
        font_size=54,
        falling_speed=5,
        animation_lengt="infinite",
    )
elif ratio >= 0.45 and ratio < 0.55:
    st.write('Halfway there!')
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 0.55 and ratio < 0.70:
    st.write('Getting closer!')
    rain(
        emoji="🌈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 0.7 and ratio < 0.8:
    st.write('Almost there!')
    rain(
        emoji="🤩",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 0.9 and ratio < 1:
    st.write("I'm excited to see you soon!")
    rain(
        emoji="🥰",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
elif ratio >= 1:
    st.write('Yeeeeeeeey you are here!')
    rain(
        emoji="💖",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
