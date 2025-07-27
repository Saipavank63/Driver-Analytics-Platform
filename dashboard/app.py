import streamlit as st
import pandas as pd

st.title("🚘 Driver Risk Dashboard")

df = pd.read_csv("/tmp/scored_data.csv")
st.dataframe(df)

high_risk = df[df["risk_score"] > 0.7]
st.subheader("⚠️ High Risk Drivers")
st.write(high_risk)
