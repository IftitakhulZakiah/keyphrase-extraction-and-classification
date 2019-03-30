from reader import Reader

if __name__ == "__main__":
    reader = Reader()
    reader.read(r"C:\Users\user\Documents\IF5282-NLP\relation-extraction\data\scienceie2017_train\train2")
    print(reader.publications[0].text)