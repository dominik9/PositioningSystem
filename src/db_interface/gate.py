

class GateModel:
    def __init__(self, name, x=0, y=0, z=0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def getJson(self):
        return {"Nazwa": self.name, "X": self.x, "Y": self.y, "Z": self.z}


    #Properties funs
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        if n is None:
            raise Exception('Name NONE')
        elif len(n) < 2:
            raise Exception('To short device name')
        elif len(n) > 20:
            raise Exception('To long device name')
        else:
            self._name = n

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            raise Exception('X is to low. {} is lower than 0'.format(x))
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            raise Exception('Y is to low. {} is lower than 0'.format(y))
        else:
            self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        if z < 0:
            raise Exception('Z is to low. {} is lower than 0'.format(z))
        else:
            self._z = z

    def __str__(self):
        return str(self.getJson())



