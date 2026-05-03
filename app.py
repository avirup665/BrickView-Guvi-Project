import streamlit as st
import pandas as pd
from db_connection import get_connection
import queries
import crud

st.set_page_config(layout="wide")
st.title("🏠 BrickView Real Estate Dashboard")

conn = get_connection()

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------
st.sidebar.header("Filters")

cities = pd.read_sql("SELECT DISTINCT City FROM listings", conn)['City']
selected_city = st.sidebar.multiselect("Select City", cities)

price_range = st.sidebar.slider("Price Range", 0, 10000000, (100000, 5000000))

property_types = pd.read_sql("SELECT DISTINCT Property_Type FROM listings", conn)['Property_Type']
selected_type = st.sidebar.multiselect("Property Type", property_types)

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_sql("SELECT * FROM listings", conn)

# Apply filters
if selected_city:
    df = df[df['City'].isin(selected_city)]

df = df[(df['Price'] >= price_range[0]) & (df['Price'] <= price_range[1])]

if selected_type:
    df = df[df['Property_Type'].isin(selected_type)]

# ---------------------------
# DASHBOARD
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Price by City")
    avg_df = pd.read_sql(queries.avg_price_by_city(), conn)
    st.bar_chart(avg_df.set_index('City'))

with col2:
    st.subheader("📈 Sales Trend")
    sales_df = pd.read_sql(queries.sales_trend(), conn)
    st.line_chart(sales_df.set_index('Month'))

# ---------------------------
# PIE CHART
# ---------------------------
st.subheader("🏘️ Property Type Distribution")
type_df = pd.read_sql(queries.property_type_distribution(), conn)
st.bar_chart(type_df.set_index('Property_Type'))

# ---------------------------
# MAP
# ---------------------------
st.subheader("📍 Map View")

# Dummy lat/long (since dataset may not have)
df['lat'] = 22.57
df['lon'] = 88.36

st.map(df[['lat', 'lon']])

# ---------------------------
# TABLE VIEW
# ---------------------------
st.subheader("📋 Listings Data")
st.dataframe(df)

# ---------------------------
# CRUD SECTION
# ---------------------------
st.subheader("🛠️ CRUD Operations")

with st.expander("Add Listing"):
    listing_id = st.number_input("Listing ID")
    address = st.text_input("Address")
    city = st.text_input("City")
    state = st.text_input("State")
    zip_code = st.text_input("Zip")
    prop_type = st.text_input("Property Type")
    price = st.number_input("Price")
    area = st.number_input("Area sqft")
    agent_id = st.number_input("Agent ID")
    date = st.text_input("Listed Date (YYYY-MM-DD)")

    if st.button("Add Listing"):
        crud.add_listing((listing_id, address, city, state, zip_code, prop_type, price, area, agent_id, date))
        st.success("Listing Added!")

with st.expander("Delete Listing"):
    del_id = st.number_input("Enter Listing ID to delete")

    if st.button("Delete"):
        crud.delete_listing(del_id)
        st.success("Listing Deleted!")

conn.close()