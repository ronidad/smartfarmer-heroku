import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Smart Farmer Group Project")
st.subheader(
    "This is a project undertaken to help farmers know the average prices of various commodities, the time they can sell their products, wheere to grow specicic commodieits and time to sell them to yield high returns"
)

Average_Prices = pd.read_csv("df_crops.csv").set_index("Produce_Variety")
# regions_to_sell= pd.read_csv("df_regisons.csv").set_index("CROPS")
months = pd.read_csv("df_crops_per_month.csv").set_index("Month")


# st.bar_chart(df)

selected_status = st.sidebar.selectbox(
    "Select Data to view",
    options=["Average Prices", "Products per county", "products per Months"],
)

if selected_status == "Average Prices":
    st.title("Average prices of various commodities")
    st.subheader("Products grouped into various categories")
    st.bar_chart(Average_Prices)

if selected_status == "products per Months":
    st.title("number of products per month")
    st.subheader("May has the ighest product hence the best month for many")
    st.bar_chart(months)
