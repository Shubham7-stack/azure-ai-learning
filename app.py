import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(base_url=os.environ["AZURE_OPENAI_BASE_URL"], api_key=os.environ["AZURE_OPENAI_API_KEY"])
deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

question = input("Ask something: ")

messages = [
{"role": "system", "content": "You are a helpful assistant. Answer briefly."},
{"role": "user", "content": question},
]

response = client.chat.completions.create(model=deployment, messages=messages)

print(response.choices[0].message.content)
print("Tokens used:", response.usage.total_tokens)