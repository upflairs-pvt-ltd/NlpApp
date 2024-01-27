import streamlit as st 
from transformers import pipeline
from time import sleep
from stqdm import stqdm

sentiment_analysis = pipeline("sentiment-analysis")


def sentiment_analyser(raw_text):
    result = sentiment_analysis(raw_text)[0]
    sentiment = result['label']

    ## Progress bar for wait some time
    for _ in stqdm(range(50), desc="Please wait a bit. The model is fetching the results !!"):
        sleep(0.1)

    if sentiment =="POSITIVE":
        st.write("""# This text has a Positive Sentiment.  ♥♥""")
    elif sentiment =="NEGATIVE":
        st.write("""# This text has a Negative Sentiment. 😤😔🙃""")
    elif sentiment =="NEUTRAL":
        st.write("""# This text seems Neutral ... 😐😑😕""")