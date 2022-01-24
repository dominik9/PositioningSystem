class SampleDataModel:
    def __init__(self, time, samples: list):
        self.time = time
        self.samples = samples

    def getJson(self):
        return {"Time": self.time, "Samples": self.samples}

    #Properties
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, t):
        if t == 0:
            raise Exception("Time = 0")
        else:
            self._time = t

    @property
    def samples(self):
        return self._samples

    @samples.setter
    def samples(self, s):
        if len(s) < 3:
           raise Exception('To few samples')
        else:
            self._samples = s

    def __str__(self):
        return str(self.getJson())
