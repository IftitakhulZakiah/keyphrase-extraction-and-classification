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
	"""
	def __init__(self, docs, filename=None):
		self._encoded_docs = self.encodeDocs(docs)
		if filename:
			self._embedding_matrix = self.loadFromFile(filename)
		else:
			self._embedding_matrix = self.createEmbeddingMatrix()

	@property
	def encoded_docs(self):
		return self._encoded_docs

	@property
	def embedding_matrix(self):
		return self._embedding_matrix

	@property
	def vocab_size(self):
		return self._vocab_size

	@property
	def max_length(self):
		return self._max_length

	def encodeDocs(self, docs):
		t = Tokenizer(filters='!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~', lower=True, split=None)
		t.fit_on_texts(docs)
		self._vocab_size = len(t.word_index) + 1
		encoded_docs = t.texts_to_sequences(docs)
		self._max_length = max([len(encoded_sent) for encoded_sent in encoded_docs])
		padded_docs = pad_sequences(encoded_docs, maxlen=self._max_length, padding='post')

		return padded_docs

	def createEmbeddingMatrix(self):
		filename = 'GoogleNews-vectors-negative300.bin'
		wordvector = gen.models.KeyedVectors.load_word2vec_format(filename, binary=True)
		embedding_dim = 300
		embedding_matrix = np.zeros((self._vocab_size, embedding_dim))
		for word, i in t.word_index.items():
		    try:
		        embedding_vector = wordvector[word] #wordvector = model dari Google
		    except:
		        embedding_vector = np.random.rand(embedding_dim)
		    embedding_matrix[i] = embedding_vector

		return embedding_matrix

	def saveToFile(self, filename):
		np.save(filename, arr=self._embedding_matrix)

	def loadFromFile(self, path):
		self._embedding_matrix = np.load(path)

	


