import json
import sys
from .mqttConect import MQTTConn
from PyQt5.QtWidgets import QApplication
from .MainGuiView import MainGuiView
from src.db_interface.testData import TestDataModel
from src.db_interface.gate import GateModel
from src.db_interface.room import RoomModel
from src.db_interface.device import DeviceModel
from src.db_interface.sampleData import SampleDataModel
from .rsssiLocalzationTest import RssiLocalizationTest
import os


class MainGuiController:
    def __init__(self):
        self.conn = None
        self.App = QApplication(sys.argv)
        self.mainGUI = None
        self.startGUI()
        self.startMQTT()
        self.guiShow()
        sys.exit(self.App.exec())

    def startGUI(self):
        self.mainGUI = MainGuiView()
        self.mainGUI.clicked_start.connect(self.clickedStart)
        self.mainGUI.clicked_stop.connect(self.clickedStop)
        self.mainGUI.clicked_loadFile.connect(self.clickedLoadFile)

    def startMQTT(self):

        self.conn = MQTTConn()
        self.conn.connect_mqtt()

    def guiShow(self):
        self.mainGUI.show()

    # Buttons funs
    def clickedStart(self):
        #TODO Sprawdzenie czy mqtt aktywny, sprawdzenie jaki typ testu
        #1. Pobranie danych
        #2. Jakie dane stworzenie modelu test model entry data
        #3. Spozób obliczeń i obliczenie w dobry sposób
        self.mainGUI.disabledAllWithoutStop()
        try:
            self.gates = self.mainGUI.getGates()
            r = self.mainGUI.getRoomDimensions()
            self.room = RoomModel(r[0], r[1], r[2])
            self.device = DeviceModel(self.mainGUI.getBeaconName())
            test_model = TestDataModel(self.device, self.gates, self.room)
            self.test = RssiLocalizationTest(test_model)
            self.conn.attach(self.test)
        except Exception as exc:
            print(exc)
            self.mainGUI.ensbleAddWithoutStop()
            return
        #TODO nowa klasa do obliczeń


    def clickedStop(self):
        # TODO clickedStop zabezpieczyć przed kliknięciem
        self.conn.detach(self.test)
        self.test.saveDataAndEnd()
        self.mainGUI.ensbleAddWithoutStop()

    def clickedLoadFile(self):
        dir_name = self.mainGUI.getFileName()
        file = "dane/" + dir_name + "/entry_data.json"
        if os.path.exists(file):
            self.test_data = self.loadFromFileAllModels(file)
            self.mainGUI.setupAllGui(self.test_data)
        else:
            pass
            #TODO Komunikat że nie ma pliku

    def loadFromFileAllModels(self, file) -> TestDataModel:
        with open(file, "r") as f:
            data_json = json.load(f)
        device = DeviceModel(data_json["Device"]["Name"])
        gates_list_jason = data_json["Gates"]
        samples_list_json = data_json["Samples"]
        gates = []
        for g in gates_list_jason:
            gate = GateModel(g["Nazwa"], float(g["X"]), float(g["Y"]), float(g["Z"]))
            gates.append(gate)
        room = RoomModel(data_json["Room"]["Width"], data_json["Room"]["Length"], data_json["Room"]["Height"])
        samples = []
        for s in samples_list_json:
            samples.append(SampleDataModel(s["Time"], s["Samples"]))
        return TestDataModel(device, gates, room, samples)


