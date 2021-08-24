import streamlit as st
import pandas as pd
import plotly.express as px


st.title("My chart")

df = pd.read_csv("df_crops.csv").set_index("Produce_Variety")

st.bar_chart(df)
