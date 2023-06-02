
from langchain.llms import AzureOpenAI
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

"""
Initialize the LLM model which is deployed in Azure
"""
def init_llm(model="gpt-35-turbo",deployment_name="gpt-35-turbo", temperature=0):
    
    llm = AzureOpenAI(deployment_name=deployment_name,  
                  model=model,
                  temperature=temperature,) 
    return llm


""" 
Lets add some personality to the model and ask questions
"""
print("------------------------------------------------------------")
print("Call directly the Azure OpenAI API and ChatCompletion API")
print("------------------------------------------------------------")

#prepare prompt
messages=[{"role": "system", "content": "You are HELPFUL assistant answering users trivia questions. Answer in clear and concise manner."},
          { "role": "user", "content": "Good morning, how are you today?" }]
       

answer = openai.ChatCompletion.create(engine = "gpt-35-turbo",
                                   messages = messages,)
print("ChatCompletion (gpt-35-turbo) :" + answer.choices[0].message.content)

print("------------------------------------------------------------")
"""
If you try to run following code, you will get an error:
openai.error.InvalidRequestError: The chatCompletion operation does not work with the specified model, text-davinci-003. 
Please choose different model and try again. You can learn more about which models can be used with each operation here: https://go.microsoft.com/fwlink/?linkid=2197993.
"""
#Error!
#answer = openai.ChatCompletion.create(engine = "text-davinci-003",
#                                   messages = messages,)


#prepare prompt with another question:
messages=[{"role": "system", "content": "You are HELPFUL assistant answering users trivia questions. Answer in clear and concise manner."},
          { "role": "user", "content": "what's string theory?" }]
       

answer = openai.ChatCompletion.create(engine = "gpt-35-turbo",
                                   messages = messages,)
print("ChatCompletion (gpt-35-turbo) :" + answer.choices[0].message.content)



print("------------------------------------------------------------")
print ("                    LangChain                              ")   
print("------------------------------------------------------------")   


#model "gpt-35-turbo"  
llm=init_llm()
answer=llm("Good morning, how are you?")
print("gpt-35-turbo: " + answer)

#model "text-davinci-003"
llm=init_llm("text-davinci-003", "text-davinci-003")
answer=llm("Good morning, how are you?")
print("text-davinci-003: "+ answer)


"""
Note: gpt-35-turbo and chatgpt-4 were trained in QnA mode, the meaning is that they are conversational models
text-davinci-003 is trained in text mode, the meaning is that it is trained to generate text: text in text out
this is why the answers are different
"""




