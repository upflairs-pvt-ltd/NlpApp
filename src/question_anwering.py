from langchain.llms import GooglePalm
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA,LLMChain
import os

load_dotenv()

api = os.getenv("GOOGLE_API_KEY")
palm = GooglePalm(api=api,temperature=0.2)


def get_respnse(question):
    prompt_template =  """You are my conversational chatbot ,generate an answer of the Given following question, 
        In the answer try to provide as much text as possible with my answer, without making much changes in my answer.
        and generated answer should be human redable and meaningfull, .

        QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["question"])

    chain = LLMChain(llm=palm,prompt=PROMPT)
    response = chain.run(question)
    return response

