import streamlit as st
import asyncio
from toolbox_sql_agent import run_toolbox_sql_agent

st.title("DSAR Text-to-SQL Agent Demo")

# Default values for UI
DEFAULT_TOOLBOX_URL = "http://127.0.0.1:5000"
DEFAULT_QUESTION = "Generate a BigQuery SQL query to retrieve all data on a customer with CM15 of 1234567890 in SORs C360, Adobe"

toolbox_url = st.text_input("Toolbox URL", value=DEFAULT_TOOLBOX_URL)
user_question = st.text_area("Enter your question:", value=DEFAULT_QUESTION)

if st.button("Run Agent"):
    with st.spinner("Running agent..."):
        responses = asyncio.run(run_toolbox_sql_agent(user_question, toolbox_url))
        st.subheader("Agent Response:")
        for text in responses:
            st.write(text)
