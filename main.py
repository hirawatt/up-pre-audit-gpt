import streamlit as st
import numpy as np

st.set_page_config("Pre-AuditGPT", "🤖", "centered")

st.header("Pre-Audit GPT")
with st.form("File Upload form"):
    files = st.file_uploader("Upload files to generate report")
    st.form_submit_button("Submit files")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.subheader("Sample questions to ask")
st.info("Are the financial statements correct?")
st.info("What are the major/minor discrepancies in the report?")
prompt = st.chat_input("Ask Pre-AuditGPT any questions")
if prompt:
    st.success(f"User has sent the following prompt: {prompt}")

with st.chat_message("assistant"):
    st.write("Sample data analysis")
    st.bar_chart(np.random.randn(30, 3))