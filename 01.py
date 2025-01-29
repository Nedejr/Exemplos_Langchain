# Primeiro Exemplo com Langchain

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI


load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

model = OpenAI()

response = model.invoke(
    input='Quem foi Alan Turing?',
    temperature=1,
    max_tokens=500,
)

print(response)

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)

messages = [
    {'role': 'system', 'content': 'Você é um assistente que fornece informações sobre figuras históricas.'},
    {'role': 'user', 'content': 'Quem foi Alan Turing?'}
]

response = model.invoke(messages)

print(response)
print(response.content)
