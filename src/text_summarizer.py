from transformers import pipeline
import json
import warnings
warnings.filterwarnings('ignore')

summarizer_pipeline = pipeline("summarization", model="Falconsai/text_summarization")

def summeraizer(raw_text,max_word_len):
    max_word_len = int(max_word_len)
    summary = summarizer_pipeline(raw_text, max_length=max_word_len, min_length=30)
    s1 = json.dumps(summary[0])
    d2 = json.loads(s1)
    result_summary = d2['summary_text']
    result_summary = '. '.join(list(map(lambda x: x.strip().capitalize(), 
                                    result_summary.split('.'))))
    return result_summary


