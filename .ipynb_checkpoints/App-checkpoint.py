import streamlit as st
import pandas as pd

import preprocessor,helper

df=preprocessor.preprocess()
user_menu=st.sidebar.radio(
    'Select an Option',
    ("Medal Tally","Overall Analysis","Country wise Analysis","Athlete wise Analysis")
)


st.dataframe(df)
if user_menu=="medal Tally":
    medal_tally=helper.medal_tally(df)
    st.dataframe(medal_tally)