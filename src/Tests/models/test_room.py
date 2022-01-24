from src.db_interface.room import RoomModel
import pytest


class TestRoom:
    def test_zero_in_room(self):
        with pytest.raises(Exception):
            room = RoomModel(0,1,0)

    def test_json(self):
        room = RoomModel(2, 3, 4)
        assert room.getJsonModel() == {"Width": 2, "Length": 3, "Height": 4}
