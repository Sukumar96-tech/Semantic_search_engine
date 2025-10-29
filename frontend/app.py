import streamlit as st
from api_client import APIClient

st.set_page_config(page_title="Semantic Search", layout="centered")
st.title("Semantic Search Engine")

client = APIClient(base_url=st.secrets.get("backend_url", "http://localhost:8000"))

query = st.text_input("Enter your query")
k = st.slider("Number of results", 1, 20, 5)
if st.button("Search"):
    if not query:
        st.warning("Please enter a query.")
    else:
        with st.spinner("Searching..."):
            resp = client.search(query, k=k)
            results = resp.get("results", [])
            if not results:
                st.info("No results found.")
            for r in results:
                st.markdown(f"**{r.get('title','[no title]')}** (score: {r.get('score'):.4f})")
                st.write(r.get("text", "")[:500])
