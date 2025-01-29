# Caching de Prompts

import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache


load_dotenv()

model = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

#set_llm_cache(InMemoryCache())

set_llm_cache(SQLiteCache(database_path='openai_cache.db'))

prompt = 'me fale sobre Alan Turing?'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2}')
