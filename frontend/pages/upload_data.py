import streamlit as st
st.write("# Upload Data")
st.write("Upload a CSV with columns: id,title,text. This feature is a placeholder - implement ingestion endpoint or upload to backend storage.")
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    st.success("File received. Please upload the CSV to the backend ingestion endpoint (not implemented in this scaffold).")
