from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai
from dotenv import load_dotenv
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

def index_documents(embeddings):
    dataPath = "./data/"
    fileName = dataPath + "fabric-data-engineering.pdf"
    loader = PyPDFLoader(fileName)
    pages = loader.load_and_split()
    db = FAISS.from_documents(documents=pages, embedding=embeddings)
    db.save_local("./dbs/documentation/faiss_index")

if __name__ == "__main__":
    embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL_NAME, chunk_size=1)
    index_documents(embeddings)
