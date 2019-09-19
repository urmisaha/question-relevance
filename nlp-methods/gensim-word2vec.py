import gensim.downloader as api

word_vectors = api.load("glove-wiki-gigaword-100")

sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
sentence_president = 'The president greets the press in Chicago'.lower().split()

similarity = word_vectors.wmdistance(sentence_obama, sentence_president)

print("gensim similarity:")
print(similarity)