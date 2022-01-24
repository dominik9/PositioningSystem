class RoomModel:
    def __init__(self, w=0, l=0, h=0):
        self.width = w
        self.length = l
        self.height = h

    def getJsonModel(self):
        return {"Width": self._width, "Length": self._length, "Height": self._height}

    #properties
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        if w < 1:
            raise Exception('Width is to low. {} is lower than 1'.format(w))
        else:
            self._width = w

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, l):
        if l < 1:
            raise Exception('Length is to low. {} is lower than 1'.format(l))
        else:
            self._length = l

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        if h < 1:
            raise Exception('Height is to low. {} is lower than 1'.format(h))
        else:
            self._height = h

