from src.db_interface.gate import GateModel
import pytest


class TestGate:
    def test_zero_if_no_arguments(self):
        gate = GateModel("Model")
        assert gate.x == 0
        assert gate.y == 0
        assert gate.z == 0

    def test_under_0(self):
        with pytest.raises(Exception):
            gate = GateModel("model", -1,1,-1)

    def test_change_x(self):
        gate = GateModel("Model")
        gate.x = 1
        assert gate.x == 1


