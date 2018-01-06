import re

def clean_sentence(cleaned_sentence):
    cleaned_sentence = re.sub(r"[\d\u0E50-\u0E59]", "0", cleaned_sentence)
    cleaned_sentence = re.sub(r'<NE>.*<\/NE>', '', cleaned_sentence)
    cleaned_sentence = re.sub(r'<AB>.*<\/AB>', '', cleaned_sentence)
    cleaned_sentence = re.sub(r'<POEM>.*<\/POEM>', '', cleaned_sentence)
    return cleaned_sentence
