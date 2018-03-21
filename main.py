import constant
import loader
import word2vec

# Use-case-01 : load existing model
word2vec_model = word2vec.Bailarn_Word2Vec()
print("Model stat:", word2vec_model.model)

# # Use-case-02 : create new model, so that can define dimension of the vector
# word2vec_model = word2vec.Bailarn_Word2Vec(new_model=True)

# # Use-case-03 : train the model
# training_set = loader.best_data_loader() + loader.free_best_data_loader() + \
#     loader.th_wiki_loader()
# word2vec_model.train(
#     training_set, model_path=constant.BASE_DIR + "/models/w2v.bin")

# Use-case-04 : predict the model
word_vector = word2vec_model.predict("สวัสดี")
print("Result shape:", word_vector.shape)

# # Use-case-05 : model evaluation
# eval_pairs = [
#     ("กิน", "นอน"),
#     ("นอน", "ง่วง"),
#     ("โรงเรียน", "โรงแรม")]
# eval_results = word2vec_model.evaluate(eval_pairs)
