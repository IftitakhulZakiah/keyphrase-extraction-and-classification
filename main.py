from reader import Reader
from wordembedder import Wordembedder
import nltk
from sentence_splitter import SentenceSplitter
from keras import regularizers
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Bidirectional
from keras.preprocessing.text import Tokenizer

def train_lstm(X, y):
    model = Sequential()
    total_token = 20
    n_timesteps = 10
    vocab_size = 300
    # model.add(Embedding(vocab_size,))
    model.add(Bidirectional(LSTM(20, return_sequence=True, input_shape=(n_timesteps, total_token))))
    model.add(Bidirectional(LSTM(20, return_sequence=True, input_shape=(n_timesteps, total_token))))
    model.add(Activation('softmax'))
    for epoch in range(100):
        model.fit(X, y, epoch=1, batch_size=20, verbose=2)
        
    model.predict_classes(X_test, verbose=0)
    # for i in range

if __name__ == "__main__":
    reader = Reader()
    reader.read(r"C:\Users\user\Documents\IF5282-NLP\relation-extraction\data\scienceie2017_train\train2")
    
    # t = Tokenizer()
    # t.fit_on_texts(docs)
    # encoded_docs = t.texts_to_sequences(docs)

    token = nltk.word_tokenize(reader.publications[0].text)
    postag = nltk.pos_tag(token)
    X = Wordembedder(reader._publications[0].text).embedding_matrix
    print(token)
    max_len = -1
    # for pub in reader.publications:
    #     sentences = SentenceSplitter(language='en').split(pub.text)
    #     for sent in sentences:
    #         length = nltk.word_tokenize(sent).length()
    #         max_len = length if length > max_len else max_len
    # print(max_len)