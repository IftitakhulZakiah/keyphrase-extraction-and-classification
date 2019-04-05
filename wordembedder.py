import gensim as gen
import tensorflow as tf
import numpy as np
from sentence_splitter import SentenceSplitter, split_text_into_sentences

class Wordembedder:
	"""
	from wordembedder import Wordembedder
	X = Wordembedder(text).tokenized_data
	"""

	def __init__(self, text):
		filename = 'GoogleNews-vectors-negative300.bin'
		self._wordvector = gen.models.KeyedVectors.load_word2vec_format(filename, binary=True, limit=500000)
		self._tokenized_data = self.embed(self.tokenize(text))

	@property
	def wordvector(self):
		return self._wordvector

	@property
	def tokenized_data(self):
		return self._tokenized_data

	def tokenize(self, text):
		tokenized_text = []
		ar_sent = SentenceSplitter(language='en').split(text)
		for sentence in ar_sent:
			tokenized_text.append(tf.keras.preprocessing.text.text_to_word_sequence(sentence, 
				filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n\xa01234567890',
				lower=True,
				split=' ')
			)
		return  tokenized_text

	def embed(self, tokenized_text):
		encoded_docs = []
		for tokenized_sent in tokenized_text:
		    encoded_sent = []
		    for term in tokenized_sent:
		        try:
		            encoded_sent.append(self._wordvector.vocab[term].index)
		        except:
		            pass
		    encoded_docs.append(encoded_sent)
		
		mx = max([len(encoded_sent) for encoded_sent in encoded_docs])
		X_w2v = tf.keras.preprocessing.sequence.pad_sequences(encoded_docs, maxlen=mx, padding='post')
		
		return X_w2v


