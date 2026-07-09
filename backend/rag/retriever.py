from .vector_store import vector_store

retriever = vector_store.as_retriever()


def retreive_documents(query: str):
    return retriever.invoke(query)


if __name__ == "__main__":
    documents = retreive_documents(
        "What are the three things every girl child should receive according to the document?")

    print(documents)
