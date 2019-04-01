from keyphrase import Keyphrase

class Publication:
    def __init__(self, filename, text, keyphrases):
        self._filename = filename
        self._text = text
        self._keyphrases = keyphrases
    
    @property
    def filename(self):
        return self._filename

    @property
    def text(self):
        return self._text

    @property
    def keyphrases(self):
        return self._keyphrases

    