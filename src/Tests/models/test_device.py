from src.db_interface.device import DeviceModel
import pytest


class TestDevice:
    def test_json_ret(self):
        device = DeviceModel("Device1")
        assert device.getJson() == {"Name": "Device1"}