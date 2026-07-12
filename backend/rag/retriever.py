import boto3
from langchain_core.documents import Document

bedrock_agent_runtime = boto3.client(
    "bedrock-agent-runtime",
    region_name="ap-south-1"
)


def retreive_documents(query: str):
    response=bedrock_agent_runtime.retrieve(
        knowledgeBaseId="LOIP2RDSQ0",
        retrievalQuery={
            "text": query,
        },
    )

    documents = []

    for result in response["retrievalResults"]:
        documents.append(
            Document(
                page_content=result["content"]["text"],
                metadata=result["metadata"],
            )
        )

    return documents


if __name__ == "__main__":
    documents = retreive_documents(
        "What are the three things every girl child should receive according to the document?")

    print(documents)
