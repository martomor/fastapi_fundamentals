import json
from pydantic import BaseModel

class Car(BaseModel): #Pydantic makes sure to parse all items into the types specified
    id: int
    size: str
    fuel: str|None = "electric" #Default values
    doors: int
    transmission: str|None = "auto"
# pydantic methods can be accesed as:
# c.json() or c.dict()

def load_db() -> list[Car]:
    """Load a list of Car objects from a JSON file"""
    with open ("cars.json") as f:
        return [Car.parse_obj(obj) for obj in json.load(f)]