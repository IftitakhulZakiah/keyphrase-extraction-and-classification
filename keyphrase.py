class Keyphrase:
    def __init__(self, id, label, start, end, surface):
        self._id = id
        self._label = label
        self._start = start
        self._end = end
        self._surface = surface
    
    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def surface(self):
        return self._surface

