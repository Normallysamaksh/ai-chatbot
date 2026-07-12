import boto3
from dotenv import load_dotenv

load_dotenv()
bedrock_agent_runtime = boto3.client(
    "bedrock-agent-runtime",
    region_name="ap-south-1",
)

response = bedrock_agent_runtime.retrieve(
    knowledgeBaseId="LOIP2RDSQ0",
    retrievalQuery={
        "text": "Summarise this document",
    }
)

print(response)
