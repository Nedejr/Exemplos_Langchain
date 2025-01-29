# Simple Chains

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatOpenAI(model='gpt-3.5-turbo', api_key=os.getenv('OPENAI_API_KEY'))

prompt_template = PromptTemplate.from_template(
    'Me fale sobre o carro {carro}.'
)

runnable_sequence = prompt_template | model | StrOutputParser()
response = runnable_sequence.invoke({'carro': 'Marea 20v 1999'})
print(response)


# OR

chain = (
    PromptTemplate.from_template('Me fale sobre o carro {carro}.')
    | model
    | StrOutputParser()
)
response = chain.invoke({'carro': 'Marea 20v 1999'})
print(response)
