from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv
import openai
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_EMBEDDING_MODEL_NAME = os.getenv("OPENAI_EMBEDDING_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = OPENAI_DEPLOYMENT_VERSION
openai.api_base = OPENAI_DEPLOYMENT_ENDPOINT
openai.api_key = OPENAI_API_KEY

def ask_question(qa, question):
    result = qa({"query": question})
    print("\n Answer:", result["result"])

if __name__ == "__main__":
    llm = AzureOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME, 
                    model_name=OPENAI_MODEL_NAME, 
                    openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT, 
                    openai_api_key=OPENAI_API_KEY)
    embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL_NAME, chunk_size=1)
    vectorStore = FAISS.load_local("./dbs/documentation/faiss_index", embeddings)
    retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False)
    while True:
        query = input('you: ')
        if query == 'q':
            break
        ask_question(qa, query)