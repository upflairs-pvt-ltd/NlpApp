from transformers import pipeline


hindi_to_english_model = "Helsinki-NLP/opus-mt-hi-en"
enlgish_to_hindi_model = "Helsinki-NLP/opus-mt-en-hi"

def translator(text,language):
    if language == "eng_to_hi":
        # Set up the translation pipeline for Hindi to English
        translator = pipeline("translation", model=enlgish_to_hindi_model)

        # Perform Hindi to English translation
        text_length = len(text)+50
        english_translation = translator(text, max_length=text_length)
        return english_translation[0]['translation_text']

    else:
        # Set up the translation pipeline for Hindi to English
        translator = pipeline("translation", model=hindi_to_english_model)

        # Perform Hindi to English translation
        text_length = len(text)+50
        hindi_translation = translator(text, max_length=text_length)
        return hindi_translation[0]['translation_text']

