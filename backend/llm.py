from dotenv import load_dotenv
from langchain_aws import ChatBedrock
load_dotenv()

llm = ChatBedrock(
    model_id="meta.llama3-70b-instruct-v1:0",
    model_kwargs={
        "temperature": 0,
    },
)
