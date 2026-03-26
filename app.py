import streamlit as st
from utils import extract_text
from rag_pipeline import rag_pipeline

st.title("🚀 AI Resume Matcher")

file = st.file_uploader("Upload Resume PDF")

if file:
    text = extract_text(file)
    result = rag_pipeline(text)
    st.write(result)