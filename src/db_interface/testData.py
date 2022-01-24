from typing import List

from .device import DeviceModel
from .gate import GateModel
from .room import RoomModel
from .sampleData import SampleDataModel
from .reciveData import ReciveDataModel
import json
import time
import copy
#Recive data format
#{"Gate":"BRAMKA2","Device":"DEVICE1","RSSI":-27}
class TestDataModel:
    def __init__(self, dev: DeviceModel, gates: List[GateModel], room: RoomModel, samples=[]):
        self.recive_data = None
        self.device = dev
        self.gates = gates
        self.room = room
        self.sample_data_list = samples
        if len(samples) == 0:
            self.addStartSamples()

    def addSample(self, data):
        try:
            self.recive_data = ReciveDataModel(data["Gate"], data["Device"], data["RSSI"], time.strftime("%Y%m%d%H%M%S"))
        except Exception as e:
            print(e)
            return
        # Zwracanie id bramki w z której są dane
        number_gate = 0
        for g in self.gates:
            if g.name == self.recive_data.gate_name:
                break
            else:
                number_gate += 1
                if number_gate > len(self.gates):
                    print("Not search gate {} in list {}".format(g.name, self.gates))
                    return
        last_sample = copy.deepcopy(self.sample_data_list[-1])
        last_sample.samples[number_gate] = self.recive_data.rssi
        actual_sample = SampleDataModel(self.recive_data.time, last_sample.samples)
        self.sample_data_list.append(actual_sample)

    def getJson(self):
        return {"Room":self.room.getJsonModel(),
                "Device":self.device.getJson(),
                "Gates": [g.getJson() for g in self.gates],
                "Samples":[s.getJson() for s in self.sample_data_list]}

    def getJsonText(self):
        return json.dumps(self.getJson())

    def addStartSamples(self):
        iter_gates = len(self.gates)
        for i in range(iter_gates):
            sample = SampleDataModel(time.strftime("%Y%m%d%H%M%S"), [0 for x in range(iter_gates)])
            self.sample_data_list.append(sample)

    #Properties
    @property
    def gates(self):
        return self._gates

    @gates.setter
    def gates(self, g):
        if len(g) < 3:
            raise Exception('To few gates')
        else:
            self._gates = g

    def __str__(self):
        return self.getJsonText()




