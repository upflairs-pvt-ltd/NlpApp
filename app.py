from src.utils import draw_all
from src.text_summarizer import summeraizer
from src.NER_extractor import Ner_extractor
from src.question_anwering import get_respnse
from src.sentiment_analysis import sentiment_analyser
from src.text_generation import complete_text
import streamlit as st 
from time import sleep
from stqdm import stqdm
import pandas as pd 
from transformers import pipeline
import json
import spacy


with st.sidebar:
    draw_all("sidebar")



def main():

    # Task list for choose
    menu = ["--Select--","Summarizer","Named Entity Recognition",
            "Sentiment Analysis","Question Answering","Text Completion"]
    choice = st.sidebar.selectbox("Choose What u wanna do !!", menu)


    ### HOME SELECT
    if choice == "--Select--":
        st.title("🦾 Unlock The Power of NLP 🦾")
        st.write("""
                 
                 This is a Natural Language Processing Based Web App that can do   
                 anything u can imagine with the Text.
        """)
        
        st.write("""
                 
                Natural Language Processing (NLP) is a computational technique
                to understand the human language in the way they spoke and write.
        """)
        
        st.write("""
                 
                 NLP is a sub field of Artificial Intelligence (AI) to understand
                 the context of text just like humans.
        """)
        
        
        st.image('image3.jpg')



    ### TEXT SUMMARIZATION
    elif choice == "Summarizer":
        st.subheader("Text Summarization")
        raw_text = st.text_area("Paste Your Text Here")
        num_words = st.number_input("Enter Number of Words in Summary")
        submit = st.button("Get Summary")
        
        if raw_text != "" and num_words is not None and submit:

            result_summary = summeraizer(raw_text,num_words)
            st.subheader("Your Summary is :")
            st.write(result_summary)


    ## NER EXTRACTOR ANALYZER CODE
    elif choice == "Named Entity Recognition":
        st.subheader("Named Entity Recognizer")
        raw_text = st.text_area("Paste Your Text Here")
        submit=st.button("Get Result")

        if raw_text !="" and submit:
            Ner_extractor(raw_text=raw_text)

    ## SENTIMENTS ANALYSER
    elif choice=="Sentiment Analysis":
        st.subheader("Sentiment Analyser")
        st.write(" Enter the Text below To find out its Sentiment !")
        raw_text = st.text_area("Paste Your Text Here")
        submit = st.button("Submit")

        if raw_text != "" and submit:
            sentiment_analyser(raw_text=raw_text)


    ### Question Answering
    elif choice == "Question Answering":
        st.subheader("Ask Your question, I am RoBo 😎")
        question=st.text_input("write your question: ",key="question")        
        submit = st.button('Get Answer')

        if submit and question != "":
            response = get_respnse(question=question)
            st.write(
                "Your Answer is :"
            )
            st.write(response)


    elif choice=="Text Completion":
        st.subheader("Complete my Text ....")
        st.write(" Enter the uncomplete Text to complete it automatically using AI !")

        text = st.text_input('write here..',key='text')
        submit = st.button('Complete my Text')
        complete_text(user_text=text,submit=submit)

if __name__ == '__main__':
     main()