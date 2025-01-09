from createS3 import create_s3_bucket 
import boto3
from botocore.exceptions import NoCredentialsError


ACCESS_KEY = input('Enter the Access Key : ')
SECRET_KEY = input('Enter the Secret Key : ')
LOCAL_FILE = input('Enter the Local File Name : ')
BUCKET_NAME = input('Enter the Bucket Name : ')
S3_FILE_NAME = input('Enter the S3 File Name : ')
region = input('Enter the region Name : ')

def upload_to_s3(local_file, bucket, s3_file):
    ## This function is responsible for uploading the file into the S3 bucket using the specified credentials. 
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


create_s3_bucket(BUCKET_NAME , region)

result = upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_FILE_NAME)
