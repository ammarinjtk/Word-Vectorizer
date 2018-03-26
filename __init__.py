from Word_Embedder.word2vec import Bailarn_Word2Vec

bailarn_word2vec_model = Bailarn_Word2Vec()


def word_to_vector(word):
    return bailarn_word2vec_model.predict(word)


__all__ = ["Bailarn_Word2Vec", "word_to_vector", "bailarn_word2vec_model"]
