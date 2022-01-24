from paho.mqtt import client as mqtt_client
import random
from .observer import Observer, Subject
from typing import List


class MQTTConn(Subject):
    _observers: List[Observer] = []
    _last_text_from_mqtt: str

    def __init__(self):
        self.broker = '192.168.0.17'
        self.port = 1883
        self.topic = "deviceRSSI"
        self.client = mqtt_client.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconect
        self.client.on_message = self.on_message
        self.term = None
        self.connect_state = 0
        self.client_id = f'python-mqtt-{random.randint(0, 100)}'

    def connect_mqtt(self):
        try:
            self.client.connect(self.broker, self.port)
            self.client.loop_start()
        except:
            print("MQTT CONNECTION FAILED")
            self._last_text_from_mqtt = "MQTT CONNECTION FAILED"
            self.notify()

    def disconnect_mqtt(self):
        self.client.disconnect()
        self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker! 192.168.0.17:1883")
            self.client.subscribe(self.topic)
            self.connect_state = 1
        else:
            print("Failed to connect, return code %d\n", rc)
            self.connect_state = 0

    def on_disconect(self, client, userdata, rc):
        print("disconnected MQTT Broker! 192.168.0.17:1883")
        self.connect_state = 0

    def on_message(self, client, userdata, msg):
        #print(f"Received `{msg.payload}` from `{msg.topic}` topic")
        self._last_text_from_mqtt = msg.payload
        self.notify()

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def get_mqtt_text(self):
        return self._last_text_from_mqtt

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def getConnStatus(self):
        return self.connect_state
