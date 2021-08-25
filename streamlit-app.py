import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Smart Farmer Group Project")

Average_Prices = pd.read_csv("df_crops.csv").set_index("Produce_Variety")
months = pd.read_csv("df_crops_per_month.csv").set_index("Month")
product_counties = pd.read_csv("df_to_products_per_county.csv").set_index("COMMODITY")
regions_to_plant = pd.read_csv("df_regions.csv").set_index("CROP")


# st.bar_chart(df)

selected_status = st.sidebar.selectbox(
    "Select Data to view",
    options=[
        "Average Prices",
        "Products in counties",
        "products per Months",
        "Regions to Grow",
    ],
)

if selected_status == "Average Prices":
    st.title("Average prices of various commodities")
    st.subheader("Products grouped into various categories")
    st.bar_chart(Average_Prices)

if selected_status == "Products in counties":
    st.title("Products per county")
    st.subheader(
        "These products gives the farmer maximum profit if they are sold in the respective counties"
    )
    st.table(product_counties)

if selected_status == "products per Months":
    st.title("number of products per month")
    st.subheader("May has the ighest product hence the best month for many")
    st.bar_chart(months)

if selected_status == "Regions to Grow":
    st.title("Regions where specific crops do yield the highest")
    st.subheader(
        "The following crops do better in these counties as per the yields per Hactare"
    )
    st.table(regions_to_plant)
