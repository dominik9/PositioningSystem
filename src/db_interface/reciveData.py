

class ReciveDataModel:
    def __init__(self, gate_name, device, rssi, time):
        self._gate_name = gate_name
        self.device = device
        self.rssi = rssi
        self.time = time

    # Properties
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
    def rssi(self):
        return self._rssi

    @rssi.setter
    def rssi(self, r):
        if r == 0:
            raise Exception("RSSI = 0")
        else:
            self._rssi = r

    @property
    def gate_name(self):
        return self._gate_name

    @gate_name.setter
    def gate_name(self, gate):
        self._gate_name = gate
