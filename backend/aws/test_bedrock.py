import boto3

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="ap-south-1"
)

response = bedrock.converse(
    modelId="meta.llama3-70b-instruct-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "reply with one word: success"
                }
            ]
        }
    ]
)

print(response)
