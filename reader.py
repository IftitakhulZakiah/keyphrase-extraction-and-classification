from publication import Publication
from keyphrase import Keyphrase
from os import listdir
from os.path import isfile, join
import os
import csv

class Reader:
    def __init__(self):
        self._publications = []
    
    @property
    def publications(self):
        return self._publications

    def read(self, path):
        txt_files = [f for f in listdir(path) if (isfile(join(path,f)) and f.endswith(".txt"))]
        self._publications = []
        for f in txt_files:
            filename = f[:-4]
            text = ""
            with open(path + '\\' + f, encoding='utf-8') as inputfile:
                for row in csv.reader(inputfile):
                    for sent in enumerate(row):
                        if sent[0] != 0:
                            text += ',' + sent[1].replace(u'\xa0', ' ')
                        else:
                            text += sent[1].replace(u'\xa0', ' ')
            keyphrases = []
            with open(path + '\\' + filename + '.ann', encoding='utf-8') as annfile:
                for row in csv.reader(annfile):
                    temp = row[0].split('\t')
                    temp_label = temp[1].split(' ')
                    if (len(temp)) == 3:
                        keyphrases.append(Keyphrase(temp[0], temp_label[0], temp_label[1], temp_label[2], temp[2]))
                    elif (len(temp)) == 2:
                        keyphrases.append(Keyphrase(temp[0], temp_label[0], temp_label[1], temp_label[2], '.')) # the dummy surface
            self._publications.append(Publication(filename, text, keyphrases))