
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Energy Monitoring", layout="wide")

st.title("📊 Smart Energy Monitoring Dashboard")

uploaded_file = st.file_uploader("Upload your energy usage CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Filters
    device_filter = st.sidebar.multiselect("Select Device(s)", df["Device"].unique(), default=df["Device"].unique())
    df = df[df["Device"].isin(device_filter)]

    st.metric("🔌 Total Energy Consumed (kWh)", f"{df['Energy (kWh)'].sum():.2f}")

    # Time series chart
    st.subheader("📈 Energy Usage Over Time")
    fig1 = px.line(df, x="Timestamp", y="Energy (kWh)", color="Device")
    st.plotly_chart(fig1, use_container_width=True)

    # Bar chart by device
    st.subheader("🔋 Energy by Device")
    df_summary = df.groupby("Device")["Energy (kWh)"].sum().reset_index()
    fig2 = px.bar(df_summary, x="Device", y="Energy (kWh)", color="Device")
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Please upload a CSV with columns: Timestamp, Device, Energy (kWh)")
