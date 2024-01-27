from langchain.llms import GooglePalm
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA,LLMChain
import streamlit as st
import json
import os

load_dotenv()

api = os.getenv("GOOGLE_API_KEY")
palm = GooglePalm(api=api,temperature=0.2)

def complete_text(user_text,submit):
    prompt_template =  """You are my Text completor ,you will complete my incomplete text,
    so generate text should be human redable and meaningfull, and related with my incomplete text .

    TEXT: {text}"""

    my_prompt = PromptTemplate(template=prompt_template,input_variables=['text'])
    chain = LLMChain(llm=palm,prompt=my_prompt)

    if user_text != "" and submit:
        response = chain.run(user_text)
        st.write(response)
