import os
import glob
from Word_Embedder.utils import clean_sentence

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
            file_sentence = [i for i in file_string.split('|') if i != ""]
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
    # Read Free BEST data
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
            file_sentence = [i for i in file_string.split('|') if i != ""]
            best_free_all_sentences.append(file_sentence)

    free_best_word_count = 0
    free_best_sentence_count = 0
    for sentence in best_free_all_sentences:
        free_best_sentence_count += 1
        free_best_word_count += len(sentence)

    print("Loader done!\n\tfree BEST data : " + str(free_best_sentence_count) + " sentences, "
          + str(free_best_word_count) + " words.")
    return best_free_all_sentences


def th_wiki_loader():
    th_wiki_all_sentences = []
    filepath_format = "./dataset/thwiki/wiki_{}"
    file_number_range = [str(i) if i >= 10 else "0" + str(i)
                         for i in range(51)]
    for file_number in file_number_range:
        filename = filepath_format.format(file_number)
        file = open(filename, 'r', encoding="utf-8")
        file_string = file.read()
        file.close()
        file_string = clean_sentence(file_string)
        file_sentence = [i for i in file_string.split('|') if i != ""]
        th_wiki_all_sentences.append(file_sentence)

    th_wiki_word_count = 0
    th_wiki_sentence_count = 0
    for sentence in th_wiki_all_sentences:
        th_wiki_sentence_count += 1
        th_wiki_word_count += len(sentence)

    print("Loader done!\n\tTH Wiki data : " + str(th_wiki_sentence_count) + " sentences, "
          + str(th_wiki_word_count) + " words.")

    return th_wiki_all_sentences
