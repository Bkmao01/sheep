from models.models import Sheep
from typing import Dict

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep]={}
    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)
    
db =FakeDB()
db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Spice2", breed="Gotland2", sex="ewe2"),
    3: Sheep(id=3, name="Spice3", breed="Gotland3", sex="ewe3"),
    4: Sheep(id=4, name="Spice4", breed="Gotland4", sex="ewe4"),
    5: Sheep(id=5, name="Spice5", breed="Gotland5", sex="ewe5"),
    6: Sheep(id=6, name="Spice6", breed="Gotland6", sex="ewe6"),

}

def add_sheep(self,sheep: Sheep) -> Sheep:
    if sheep.id in self.data:
        raise ValueError("Id exsist")
    self.data[sheep.id] = sheep
    return sheep