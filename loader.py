import os, glob
from utils import clean_sentence

# GetCWD
base_dir = os.path.dirname(os.path.abspath(__file__))

def best_data_loader():
    # Read BEST data
    best_path_list = [base_dir + "/dataset/BEST2010/Train"]
    best_all_sentences = []
    for path in best_path_list:
        for filename in glob.glob(os.path.join(path, '*.txt')):
            file = open(filename, 'r', encoding="utf-8")
            file_string = file.read()
            file.close()
            file_string = clean_sentence(file_string)
            file_sentence = file_string.split('|')
            temp_sentence = []
            for sentence in file_sentence:
                temp_sentence.append(sentence.split('/')[0])
            best_all_sentences.append(temp_sentence)

    best_word_count = 0
    best_sentence_count = 0
    for sentence in best_all_sentences:
        best_sentence_count += 1
        best_word_count += len(sentence)

    print("Loader done!\n\tBEST data : " + str(best_sentence_count) + " sentences, "
          + str(best_word_count) + " words.")
    return best_all_sentences


def free_best_data_loader():
    """ Read Free BEST data """
    best_free_path_list = [
        base_dir + "/dataset/BEST_data/news/",
        base_dir + "/dataset/BEST_data/encyclopedia/",
        base_dir + "/dataset/BEST_data/novel/",
        base_dir + "/dataset/BEST_data/article/"]
    best_free_all_sentences = []
    for path in best_free_path_list:
        for filename in glob.glob(os.path.join(path, '*.txt')):
            file = open(filename, 'r', encoding="utf-8")
            file_string = file.read()
            file.close()
            file_string = clean_sentence(file_string)
            best_free_all_sentences.append(file_string.split('|'))

    free_best_word_count = 0
    free_best_sentence_count = 0
    for sentence in best_free_all_sentences:
        free_best_sentence_count += 1
        free_best_word_count += len(sentence)

    print("Loader done!\n\tfree BEST data : " + str(free_best_sentence_count) + " sentences, "
          + str(free_best_word_count) + " words.")
    return best_free_all_sentences



