import streamlit as st
import json
import datetime
import os
from src.upload_and_process import upload_to_s3, start_textract_job, get_textract_results
from src.preprocess import preprocessdata
from src.db import create_db, insert_record, show_alldata

# Set up the Streamlit page
st.title("PDF Upload and Textract Processing")

# Allow users to upload a PDF file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

bucket_name = 'inputfolder2' 

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

        folder_path = 'output'
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'w') as file:
            json.dump(results, file, indent=4)

        a,b,c,d,e,f,g,h,i,j,k,l = preprocessdata(results)
        print(a,b,c,d,e,f,g,h,i,j,k,l)

        st.success("Document processed successfully!")

        create_db()
        insert_record(a,b,c,d,e,f,g,h,i,j,k,l)
        show_alldata()

    except Exception as e:
        st.error(f"An error occurred: {e}")