from src.db_interface.testData import TestDataModel
from src.db_interface.reciveData import ReciveDataModel
from .observer import Observer, Subject
import json
import time
import os

#TODO Cała klasa do zaprogramowania
#1. określenie skąd dane i działanie w odpowiedni sposób, dodać nową wartość wejściowe rodzaj obliczeń i czy z pliku
#2. Jeżeli z pliku to pętla obliczeń z czasem który jest zapisany
#3. Dodanie wyświetlania wizualizacji ale to jako nowa klasa wywoływana stąd
class RssiLocalizationTest(Observer):
    def __init__(self, test_data: TestDataModel):
        self.test_data = test_data

    def update(self, subject: Subject):
        mqtt_frame_text = subject.get_mqtt_text()
        print(mqtt_frame_text)
        mqtt_frame_json = json.loads(mqtt_frame_text)
        self.test_data.addSample(mqtt_frame_json)
        #TODO tutaj rozpoczęcie obliczeń ostatniej próbki

    def saveDataAndEnd(self):
        file_dir = "dane/%s" % (time.strftime("%Y%m%d%H%M%S"))
        os.mkdir(file_dir)
        file_name = file_dir + "/entry_data.json"
        with open(file_name, "w") as file:
            file.write(self.test_data.getJsonText())

