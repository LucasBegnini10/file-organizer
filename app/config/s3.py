import boto3
import os

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)