import os
import boto3
from dotenv import load_dotenv

env_path = '/Users/ayushkumar/Desktop/portfolio_workspace/myportfolio/.env'
load_dotenv(env_path)

# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME
)

media_dir = '/Users/ayushkumar/Desktop/portfolio_workspace/media'

def upload_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, media_dir)
            print(f"Uploading {local_path} to {relative_path}...")
            try:
                s3.upload_file(local_path, AWS_STORAGE_BUCKET_NAME, relative_path)
                print(f"Uploaded {file} successfully.")
            except Exception as e:
                print(f"Failed to upload {file}: {e}")

if __name__ == "__main__":
    upload_files(media_dir)
