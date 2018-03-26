import gensim
import os
import numpy as np
from Word_Embedder.utils import find_low_freq_words
from Word_Embedder.constant import BASE_DIR, DEFULT_MODEL_PATH, UNKNOWN_WORD, VECTOR_DIMENSION, CBOW_SG_FLAG


class Bailarn_Word2Vec(object):
    """ A Word2Vec is defined as Word embedding model containing of
            - Word2Vec (implemented by gensim) :
                input format : list of string (e.g. ["ฉัน", "กิน", "ข้าว"])
                output format : list of vectors has length which equals the number of words (e.g. [v1, v2, v3])

                Moreover, Word2Vec is trained by data which are BEST_data, free BEST_data, Pantip posts, TED_thai.txt
                by input format such as [s1, s2, s3]
                which s1, s2, s3 are defined to be sentence (list of words). For example, s1 can be ["ฉัน", "เดิน"].

                To handle unseen word, the model uses low frequent word vectors instead.
    """

    def __init__(self, model_path=None, new_model=False):
        self.new_model = new_model

        if not new_model:
            if model_path is not None:
                self.model = gensim.models.Word2Vec.load(model_path)
            else:
                self.model = gensim.models.Word2Vec.load(DEFULT_MODEL_PATH)
        else:
            # sg=1 means to use skip-gram technique
            self.model = gensim.models.Word2Vec(
                size=VECTOR_DIMENSION, sg=CBOW_SG_FLAG)

    def train(self, sentences, update=True, model_path=DEFULT_MODEL_PATH):
        """
            Parameter :
                pre_process is to transform any raw string ("ฉันกินข้าว") into one training sentence (["ฉัน", "กิน", "ข้าว"])
                update is to build initial vocab for the model or update it

            Word2Vec model is implemented by gensim library with default parameters
        """

        # find all low frequency words, then change it to be "UNK"
        low_freq_word = find_low_freq_words(sentences, threshold=5)

        total_count = 0
        for sentence in sentences:
            total_count += len(sentence)
        count = 0
        print_threshold = 10000
        threshold_count = 0
        total_count = int(total_count / print_threshold)
        for lst in sentences:
            for ind, item in enumerate(lst):
                count += 1
                lst[ind] = low_freq_word.get(item, item)
                if count >= print_threshold:
                    count = 0
                    print(threshold_count, "/", total_count)
                    threshold_count += 1

        # for i, sentence in enumerate(sentences):
        #     for j, word in enumerate(sentence):
        #         if word in low_freq_word_list:
        #             count += 1
        #             sentences[i][j] = UNKNOWN_WORD
        #         if count >= print_threshold:
        #             count = 0
        #             print(threshold_count, "/", total_count)
        #             threshold_count += 1
        # If new_model (empty) then the model should first build the vocab, update=False
        print("Start training model.")
        for sentence in sentences:
            if UNKNOWN_WORD in sentence:
                print("UNK is here!")
                break
        update = not self.new_model
        self.model.build_vocab(sentences, update=update)
        if update:
            self.model.train(
                sentences, total_examples=self.model.corpus_count, epochs=self.model.iter)
        else:
            self.model.train(sentences)
        print("Saving model.")
        self.model.save(model_path)

    def predict(self, word):

        try:
            self.model[word]
        except KeyError:
            # print("{} not found! the vector will be unknown word instead.".format(sentence))
            return self.model[UNKNOWN_WORD]
        else:
            return self.model[word]

    def evaluate(self, pairs):
        # This expects input to be list of pairs of word, ex. [("กิน", "รับประทาน"), ("นอน", "หลับ")]
        # and will return the list of those pairs with similarity
        ret = []
        for (first_word, second_word) in pairs:
            # check if the word is in vocab
            try:
                self.model[first_word]
            except KeyError:
                print("The word {} is not in vocabulary !".format(first_word))
            else:
                try:
                    self.model[second_word]
                except KeyError:
                    print("The word {} is not in vocabulary !".format(second_word))
                else:
                    ret.append(
                        (first_word, second_word, self.model.wv.similarity(first_word, second_word)))
        return ret
