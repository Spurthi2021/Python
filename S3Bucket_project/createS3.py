#Program to create S3 buckets

from botocore.exceptions import ClientError
import boto3

def create_s3_bucket(bucket_name, region):
    try:
# Set up Ec2 client
        s3_client = boto3.client('s3', region_name=region)  # Replace 'us-east-1' with your desired region

#If Region is none

        if(region is None):
            s3_client.create_bucket(Bucket=bucket_name)
            
        else:
            Location = {'LocationConstraint' : region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=Location)
            print("Bucket Created")

        print(f"Bucket '{bucket_name}")
        return True
    
    except ClientError as e:
        print(f"Error: {e}")
        return False
        



#create_s3_bucket("my-unique-bucket-01-08-2025","eu-north-1")