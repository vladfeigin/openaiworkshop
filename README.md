# OpenAI workshop 

⚡ Build OpenAI applications to search your own data ⚡
This agenda covers a range of topics, from the basics of LLMs and GPT to more advanced topics like prompt engineering and embeddings. The labs provide hands-on experience with OpenAI, including connecting to the platform, creating prompts, and working with embeddings. The final lab even allows participants to ask SQL database questions in English, demonstrating the power of OpenAI in natural language processing.

## Agenda

### Morning (9:00 - 12:00)
- Theory: Introduction to LLMs, GPT and prompts - (30 mins)
- Lab #1 : Connect to OpenAI and ask questions
- Theory: Prompt engineering, Zero-shot learning, Few-shot learning (30 mins)
- Lab #2 : Create prompts for summarization, json, tabular answer
### Afternoon (13:00 - 17:00)
- Theory : Embeddings (30 mins)
- Lab #3 : Create embeddings in pandas
- Theory: Langchain, Vector databases, agents, toolkits (30 mins)
- Lab #4: Create embeddings with Faiss and Langchain
- Lab #5: Ask your SQL DB questions in English


## Requirements
- VsCode
- Python 3.7
- An Azure account with admin capabilities
- An active Azure OpenAI account

## Preparation

## OpenAI subscription and deployments
* Create an Azure OpenAI account
* Create 'gpt-35-turbo' and 'text-embedding-ada-002' deployments

### VsCode
* Install [Visual Studio Code](https://code.visualstudio.com/)

### Python
* Install [Python 3.7](https://www.python.org/downloads/release/python-31011/)

### Python3 Virtualenv Setup
*  Installation
        To install virtualenv via pip run:
            $ pip3 install virtualenv
* Creation of virtualenv:
    - Windows
    $ python -m virtualenv venv (in the openAI workshop directory)
    - Mac
    $ virtualenv -p python3 <desired-path>

    Activate the virtualenv:
    $ source <desired-path>/bin/activate

    Deactivate the virtualenv:
    $ deactivate


### Setup environemnt variables
* Edit the `.env` file including Azure OpenAI endpoint and key before starting any coding

### Install all libraries
* Make sure you have the requirements installed in your Python environment using `pip install -r requirements.txt`.
