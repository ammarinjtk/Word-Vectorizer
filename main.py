from word2vec import WordEmbedder

# Use-case-01 : load existing model
word_embedder = WordEmbedder()

# # Use-case-02 : create new model, so that can define dimension of the vector
# word_vectorizer = Wordvectorizer(pre_train=False, vector_dimension=100)

# Use-case-03 : train the model
word_embedder.train([["ฉัน", "กิน", "ข้าว"], ["เรา", "กิน", "ข้าว"]])

# Use-case-04 : predict the model
word_vector = word_embedder.predict("สวัสดี")

# Use-case-05 : model evaluation
eval_pairs = [
    ("กิน", "นอน"),
    ("นอน", "ง่วง"),
    ("โรงเรียน", "โรงแรม")]
eval_results = word_embedder.evaluate(eval_pairs)
