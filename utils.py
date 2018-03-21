import re
from functools import reduce


def clean_sentence(cleaned_sentence):
    cleaned_sentence = re.sub(r" ", "", cleaned_sentence)
    cleaned_sentence = re.sub(r"\n", "", cleaned_sentence)
    cleaned_sentence = re.sub(r"[\d\u0E50-\u0E59]", "0", cleaned_sentence)
    repls = {'<NE>': '', '</NE>': '', '<AB>': '',
             '</AB>': '', '<POEM>': '', '</POEM>': ''}
    cleaned_sentence = reduce(lambda a, kv: a.replace(
        *kv), repls.items(), cleaned_sentence)
    # cleaned_sentence = re.sub(r'<NE>.*<\/NE>', '', cleaned_sentence)
    # cleaned_sentence = re.sub(r'<AB>.*<\/AB>', '', cleaned_sentence)
    # cleaned_sentence = re.sub(r'<POEM>.*<\/POEM>', '', cleaned_sentence)
    return cleaned_sentence


def find_low_freq_words(all_sentences, threshold=5):
    count_dict = {}
    for sentence in all_sentences:
        for word in sentence:
            try:
                count_dict[word]
            except KeyError:
                count_dict[word] = 1
            else:
                count_dict[word] += 1

    low_freq_words = []
    for key, value in count_dict.items():
        if value < threshold:
            low_freq_words.append(key)
    print(len(low_freq_words))
    print(low_freq_words)
    return low_freq_words
