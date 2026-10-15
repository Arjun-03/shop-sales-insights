"""Shop Sales Insights: application entry point.

Run from the project folder with:
    streamlit run app.py
"""

from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

# All dates in the app use Sri Lanka time, regardless of the computer's settings.
SHOP_TIMEZONE = ZoneInfo("Asia/Colombo")

st.set_page_config(page_title="Shop Sales Insights", page_icon="🛒")

now = datetime.now(SHOP_TIMEZONE)
print(f"Script ran at {now:%H:%M:%S}")

st.title("Shop Sales Insights")
st.write(f"Today is **{now:%A, %d %B %Y}** (Sri Lanka time).")

st.divider()

st.subheader("How Streamlit reruns your script")
amount = st.number_input("Type any number and press Enter", min_value=0, step=1)
st.write(f"You entered: {amount}")
st.caption(
    f"This page was generated at {now:%H:%M:%S}. "
    "Change the number and watch this time update."
)