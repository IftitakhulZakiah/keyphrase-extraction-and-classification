import gensim as gen
import tensorflow as tf
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

class Wordembedder:
	"""
	How to 
	from wordembedder import Wordembedder
	X = Wordembedder(docs).embedding_matrix
	
	docs = list of sentence in document
	example:
	docs = ['this is sentence 1',
		'this is sentence 2',
		'this is last sentence'
		]
	"""
	def __init__(self, docs):
		filename = 'GoogleNews-vectors-negative300.bin'
		self._wordvector = gen.models.KeyedVectors.load_word2vec_format(filename, binary=True)
		self._embedding_matrix = self.createEmbeddingMatrix(docs)

	@property
	def wordvector(self):
		return self._wordvector

	@property
	def embedding_matrix(self):
		return self._embedding_matrix

	def createEmbeddingMatrix(self, docs):
		t = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\xa001234567890', lower=True)
		t.fit_on_texts(docs)
		vocab_size = len(t.word_index) + 1
		encoded_docs = t.texts_to_sequences(docs)
		max_length = max([len(encoded_sent) for encoded_sent in encoded_docs])
		padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
		embedding_dim = 300
		embedding_matrix = np.zeros((vocab_size, embedding_dim))
		for word, i in t.word_index.items():
		    try:
		        embedding_vector = wordvector[word] #wordvector = model dari Google
		    except:
		        embedding_vector = np.random.rand(embedding_dim)
		    embedding_matrix[i] = embedding_vector

		return embedding_matrix


	


