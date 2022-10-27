import json
from pydantic import BaseModel

class CarInput(BaseModel): #Pydantic makes sure to parse all items into the types specified
    size: str
    fuel: str|None = "electric" #Default values
    doors: int
    transmission: str|None = "auto"
# pydantic methods can be accesed as:
# c.json() or c.dict()

class CarOutput(CarInput):
    id:int

def load_db() -> list[CarOutput]:
    """Load a list of Car objects from a JSON file"""
    with open ("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]

def save_db(cars: list[CarOutput]):
    with open("cars.json", "w") as f:
        json.dump([car.dict() for car in cars], f, indent=4)