# Azure AI Learning

My journey from Azure Administrator to Azure AI Engineer, built in public.

## What is in this repo
- python-practice/: Python exercises from Phase 1 (100 Days of Python)
- app.py: a terminal script that sends a question to an Azure OpenAI deployment and prints the answer

## Requirements
- Python 3
- An Azure Foundry resource with a deployed chat model

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```
Then open `.env` and fill in your endpoint, key and deployment name.

## Run
```
python3 app.py
```

## Notes
Never commit .env. It contains your API key.