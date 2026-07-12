from dotenv import load_dotenv
from langchain_aws import ChatBedrock
load_dotenv()

llm = ChatBedrock(
    model_id="amazon.nova-lite-v1:0",
    model_kwargs={
        "temperature": 0,
    },
)
