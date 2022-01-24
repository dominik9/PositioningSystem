import time
import os
from src.db_interface.testData import TestDataModel
from src.db_interface.gate import GateModel
from src.db_interface.device import DeviceModel
from src.db_interface.room import RoomModel
import json

sample1 = {"Gate":"BRAMKA2","Device":"DEVICE1","RSSI":-27}
sample2 = {"Gate":"BRAMKA3","Device":"DEVICE1","RSSI":-26}
sample3 = {"Gate":"BRAMKA4","Device":"DEVICE1","RSSI":-28}
samples = [sample1, sample2, sample3]

gate1 = GateModel("BRAMKA2", 1, 1, 1)
gate2 = GateModel("BRAMKA3", 1, 1, 1)
gate3 = GateModel("BRAMKA4", 1, 1, 1)
gates = [gate1, gate2, gate3]

device = DeviceModel("DEVICE1")
room = RoomModel(4.0, 6.0, 3.5)

test_data = TestDataModel(device, gates, room)
for sample in samples:
    test_data.addSample(sample)
    time.sleep(1)

print(test_data)
file_dir = "../dane/%s" % (time.strftime("%Y%m%d%H%M%S"))
os.mkdir(file_dir)
file_name = file_dir + "/entry_data.json"
with open(file_name, 'w') as file:
    file.write(test_data.getJsonText())




