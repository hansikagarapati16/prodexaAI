import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="Prodexa AI",
    layout="wide"
)

st.title("🧠 Prodexa AI – Product Discovery & Requirements Intelligence")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Input", "Analysis"])

# Home Page
if page == "Home":
    st.subheader("Welcome to Prodexa AI")
    st.write("""
        This is your AI-powered product discovery assistant.
        Upload raw input (meeting notes, feedback, tickets etc.) 
        and the system will convert it into insights, requirements, and roadmaps.
    """)

# Input Page
elif page == "Input":
    st.subheader("Upload or Paste Text Input")

    uploaded_file = st.file_uploader("Upload a text file", type=["txt", "md"])
    text_input = st.text_area("Paste text here", height=300)

    if uploaded_file:
        text_input = uploaded_file.read().decode("utf-8")

    st.session_state["raw_input"] = text_input
    if text_input:
        st.success("Input loaded successfully.")

# Analysis Page (placeholder)
elif page == "Analysis":
    st.subheader("Run Discovery Analysis")
    st.write("This will eventually run LLM-based discovery analysis.")
    st.write("Raw Input:")
    st.code(st.session_state.get("raw_input", ""), language="markdown")
