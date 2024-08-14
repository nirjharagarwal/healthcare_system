import streamlit as st
from PyPDF2 import PdfReader
import os

# Set up the Streamlit page
st.title("PDF Upload and Processing")

# Allow users to upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Perform Textract analysis on the uploaded file
    try:
        response = analyze_document(uploaded_file)
        st.success("PDF processed successfully!")
        st.json(response)  # Display the JSON response from Textract
    except Exception as e:
        st.error(f"An error occurred: {e}")
