import streamlit as st
import json
import datetime
import os
from src.upload_and_process import upload_to_s3, start_textract_job, get_textract_results
from src.preprocess import preprocessdata

# Set up the Streamlit page
st.title("PDF Upload and Textract Processing")

# Allow users to upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

bucket_name = 'inputfolder' 

if uploaded_file is not None:
    object_name = uploaded_file.name  # Use the original file name

    try:
        # Upload the file to S3
        s3_url = upload_to_s3(uploaded_file, bucket_name, object_name)
        st.write(f"File uploaded to S3: {s3_url}")

        # Start Textract job
        job_id = start_textract_job(bucket_name, object_name)
        st.write(f"Textract job started. Job ID: {job_id}")

        # Poll for Textract job completion and get results
        results = get_textract_results(job_id)
        
        # Display the JSON response
        st.json(results)

        data = 'result'
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{data}_{timestamp}.json"

        with open(filename, 'w') as json_file:
            json.dump(results, json_file, indent=4)

        a,b,c,d,e,f,g,h,i,j,k,l = preprocessdata(results)
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)

        st.success("Document processed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")