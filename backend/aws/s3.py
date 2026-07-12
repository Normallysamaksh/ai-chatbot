import os
import boto3

BUCKET_NAME = "samaksh-ai-chatbot-pdfs"

s3 = boto3.client("s3")


def list_pdfs():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    pdfs = []

    for obj in response.get("Contents", []):
        key = obj["Key"]

        if key.lower().endswith(".pdf"):
            pdfs.append(key)

    return pdfs


def download_pdf(key, destination):
    s3.download_file(
        BUCKET_NAME,
        key,
        destination
    )
