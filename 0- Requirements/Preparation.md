For this workshop you MUST have the following:

## Requirements
- VsCode
- Python 3.7
- A virtual environment tool (venv)
- An Azure account 
- An active Azure OpenAI account with 2 deployed models see below

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
* Edit the `.env` file including Azure OpenAI endpoint and key before starting any coding to include the following:
OPENAI_DEPLOYMENT_ENDPOINT ="<your openai endpoint>" 
OPENAI_API_KEY = "<your openai api key>"
OPENAI_DEPLOYMENT_NAME = "<your gpt35 deployment name>"
OPENAI_DEPLOYMENT_VERSION = "<gpt35 api version>"
OPENAI_MODEL_NAME="<gpt35 model name>"

OPENAI_EMBEDDING_DEPLOYMENT_NAME = "<your text embedding ada deployment name>"
OPENAI_EMBEDDING_MODEL_NAME = "<your text embedding ada model name>"

SQL_SERVER="<demo sql server>"
SQL_USER="<sql user>"
SQL_PWD="<sql pwd>"
SQL_DBNAME="<db name>"

#### Python3 Virtualenv Setup
*  Installation
        To install virtualenv via pip run:
            $ pip3 install virtualenv
* Creation of virtualenv:
    - Windows
    $ python -m virtualenv venv (in the openAI workshop directory)
    - Mac
    $ virtualenv -p python3 <desired-path>

### Install all libraries in your virtual environment
* Activate the environment
    Windows:
        .\venv\Scripts\activate.ps1
    Mac:
    $ source ./venv/bin/activate

* Make sure you have the requirements installed in your Python environment using `pip install -r requirements.txt`.
