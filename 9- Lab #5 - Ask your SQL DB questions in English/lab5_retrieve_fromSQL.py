from langchain import SQLDatabase
from langchain.llms import AzureOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
import openai
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_USER = os.getenv("SQL_USER")
SQL_PWD = os.getenv("SQL_PWD")
SQL_DBNAME = os.getenv("SQL_DBNAME")

# Configure OpenAI API
openai.api_type = "azure"
openai.api_version = OPENAI_DEPLOYMENT_VERSION
openai.api_base = OPENAI_DEPLOYMENT_ENDPOINT
openai.api_key = OPENAI_API_KEY

def ask_question(agent_executor, question):
    answer = agent_executor.run(question)
    pos = answer.find("Question:")
    if pos > 0:
        answer = answer[0:pos]
    pos = answer.find("<|im_end|>")
    if pos > 0:
        answer = answer[0:pos]
    print("\n Answer:", answer)

if __name__ == '__main__':
    llm = AzureOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME, model_name=OPENAI_MODEL_NAME)
    sqlconn = f"mssql+pymssql://{SQL_USER}:{SQL_PWD}@{SQL_SERVER}:1433/{SQL_DBNAME}"
    db = SQLDatabase.from_uri(sqlconn)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )
    while True:
        query = input('you: ')
        if query == 'q':
            break
        ask_question(agent_executor, query)