import pandas as pd
import numpy as np
from dotenv import load_dotenv
import openai
import pandas as pd
from openai.embeddings_utils import cosine_similarity, get_embedding
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

datafile_path = "data/recipes_onecol_with_embeddings.csv"
df = pd.read_csv(datafile_path)
df["embedding"] = df.embedding.apply(eval).apply(np.array)


def ask_question(question):
    n=1
    question_embedding = get_embedding(
        question,
        engine=OPENAI_EMBEDDING_DEPLOYMENT_NAME
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, question_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )
    answer =  ' '.join(results.Recipe.tolist()) 
    print("Answer:", answer)

if __name__ == "__main__":
    while True:
        query = input('you: ')
        if query == 'q':
            break
        ask_question(query)