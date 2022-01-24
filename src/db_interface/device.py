class DeviceModel:
    def __init__(self, n):
        self.name = n

    def getJson(self):
        return {"Name": self.name}

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
