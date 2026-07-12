import boto3
from dotenv import load_dotenv

load_dotenv()
bedrock_agent_runtime = boto3.client(
    "bedrock-agent-runtime",
    region_name="ap-south-1",
)

response = bedrock_agent_runtime.retrieve_and_generate(
    input={
        "text": "summarise this document"
    },
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "LOIP2RDSQ0",
            "modelArn": (
                "arn:aws:bedrock:ap-south-1::foundation-model/"
                "meta.llama3-70b-instruct-v1:0"
            ),
        },
    },
)

print(response)
