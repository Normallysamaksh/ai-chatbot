from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .retriever import retreive_documents
from ..llm import llm

prompt = PromptTemplate.from_template(""""
    Answer the following question using only the provided context.
    
    context:
    {context}
                                      
    question:
    {question}                                                                                                    
""")

chain = prompt | llm | StrOutputParser()

def rag_chain(question: str):
    documents = retreive_documents(question)
    context = "/n/n".join(
        document.page_content for document in documents
    )

    return chain.invoke({
        "context": context,
        "question": question,
    })

if __name__ == "__main__":
    answer = rag_chain(
        "What advice does this document give to parents?"
    )

    print(answer)

    

    


