from dotenv import load_dotenv
from openai.embeddings_utils import get_embedding
import tiktoken
import openai
import pandas as pd
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

# embedding model parameters
# encoding for text-embedding-ada-002
embedding_encoding = "cl100k_base"  
# the maximum for text-embedding-ada-002 is 8191
max_tokens = 8000 
# the number of reviews to embed
top_n = 1000

input_datapath = "./data/recipes_onecol.csv"  
df = pd.read_csv(input_datapath)
encoding = tiktoken.get_encoding(embedding_encoding)

# skip Recipes that are too long to embed > max_tokens
df["n_tokens"] = df.Recipe.apply(lambda x: len(encoding.encode(x)))
df = df[df.n_tokens <= max_tokens].tail(top_n)

# This may take a few minutes
df["embedding"] = df.Recipe.apply(lambda x: get_embedding(x, engine=OPENAI_EMBEDDING_MODEL_NAME))
df.to_csv("./data/recipes_onecol_with_embeddings.csv")

