import streamlit as st
from dotenv import load_dotenv
import os
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


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
    st.subheader("Run Discovery & RCA Analysis")

    user_input = st.session_state.get("raw_input", "")

    if not user_input:
        st.warning("Please enter input on the Input page.")
    else:
        if st.button("Run Discovery Analysis"):
            with st.spinner("Generating insights..."):
                from app.utils.analysis_engine import run_discovery_analysis
                result = run_discovery_analysis(user_input)
                st.markdown(result)

        if st.button("Run Root Cause Analysis"):
            with st.spinner("Analyzing root causes..."):
                from app.utils.analysis_engine import run_rca_analysis
                result = run_rca_analysis(user_input)
                st.markdown(result)
