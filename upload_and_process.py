import boto3
import time
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Initialize AWS clients
s3_client = boto3.client('s3', region_name='us-east-1')
textract_client = boto3.client('textract', region_name='us-east-1')

def upload_to_s3(file, bucket_name, object_name):
    """Upload a file to S3 and return the S3 URL."""
    try:
        s3_client.upload_fileobj(file, bucket_name, object_name)
        s3_url = f"s3://{bucket_name}/{object_name}"
        return s3_url
    except (NoCredentialsError, PartialCredentialsError) as e:
        raise Exception(f"Error uploading file to S3: {e}")

def start_textract_job(bucket_name, object_name):
    """Start a Textract job and return the JobId."""
    response = textract_client.start_document_text_detection(
        DocumentLocation={'S3Object': {'Bucket': bucket_name, 'Name': object_name}}
    )
    return response['JobId']

def get_textract_results(job_id):
    """Poll for Textract job completion and return the results."""
    while True:
        response = textract_client.get_document_text_detection(JobId=job_id)
        status = response['JobStatus']
        if status == 'SUCCEEDED':
            return response
        elif status == 'FAILED':
            raise Exception("Textract job failed.")
        else:
            time.sleep(10)  # Wait before polling again
