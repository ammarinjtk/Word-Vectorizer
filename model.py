import gensim
import os
import deepcut
import numpy as np
from loader import best_data_loader, free_best_data_loader
from utils import clean_sentence

class Wordvectorizer(object):
    """ A Wordvectorizer is defined as 2 functional models (Tokenizer and Word2Vec).
        Overall, the Wordvectorizer can described by
        input : any string (comment) (e.g. "ฉันกินข้าว" which is separated to 3 words based on deepcut)
        output : list of vectors with customized-length of dimension (default 100)
                    e.g. "ฉันกินข้าว" will return list of vectors (length 3) [v1, v2, v3]
                            v1, v2, v3 referred to each word vector.

        In addition, the Wordvectorizer contains of
            - Tokenizer (implemented by deepcut) :
                input format : any string (e.g. "ฉันกินข้าว")
                output format : list of tokenized string (e.g. ["ฉัน", "กิน", "ข้าว"])
            - Word2Vec (implemented by gensim) :
                input format : list of string (e.g. ["ฉัน", "กิน", "ข้าว"])
                output format : list of vectors has length which equals the number of words (e.g. [v1, v2, v3])

                Moreover, Word2Vec is trained by data which are BEST_data, free BEST_data, Pantip posts, TED_thai.txt
                by input format such as [s1, s2, s3]
                which s1, s2, s3 are defined to be sentence (list of words). For example, s1 can be ["ฉัน", "เดิน"].

                To handle unseen word, the model uses default zero vector.
    """

    def __init__(self, load=True):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.vector_dimension = 100
        if load:
            self.model = gensim.models.Word2Vec.load(self.base_dir + '/models/word_vectorizer.bin')
        else:
            self.model = gensim.models.Word2Vec(min_count=1, sg=1)
        self.sentence = ""
        self.tokenized_sentence = ""
        self.sentence_vectors = []

    def train(self, sentences, pre_process=False, update=False):
        """
            Parameter :
                pre_process is to transform any raw string ("ฉันกินข้าว") into one training sentence (["ฉัน", "กิน", "ข้าว"])
                update is to build initial vocab for the model or update it

            Word2Vec model is implemented by gensim library with default parameters
        """
        if pre_process:
            self.sentence = sentences
            self.tokenized_sentence = deepcut.tokenize(clean_sentence(self.sentence))
            training = [self.tokenized_sentence]
        else:
            training = sentences

        self.model.build_vocab(training, update=update)
        self.model.train(training, total_examples=self.model.corpus_count, epochs=self.model.iter)
        self.model.save(self.base_dir + '/models/word_vectorizer.bin')

    def predict(self, sentence, is_train=False):
        self.sentence = sentence
        self.tokenized_sentence = deepcut.tokenize(clean_sentence(sentence))

        print("sentence:", self.sentence)
        print("tokenized sentence:", self.tokenized_sentence)

        # Train new sentences
        if is_train:
            self.train([self.tokenized_sentence], update=True)

        for sentence in self.tokenized_sentence:
                try:
                    self.model[sentence]
                except KeyError:
                    print("{} not found! the vector will be zeros instead.".format(sentence))
                    self.sentence_vectors.append(np.zeros(self.vector_dimension))
                else:
                    self.sentence_vectors.append(self.model[sentence])

        return self.sentence_vectors

    def evaluate(self):
        pass

# word_vectorizer = Wordvectorizer()
# for sentence_vector in word_vectorizer.predict("เรากินข้าว เธอกินข้าว"):
#     print(type(sentence_vector))
#     print(sentence_vector.shape)

