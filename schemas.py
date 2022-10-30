import json
from sqlalchemy import table
from sqlmodel import SQLModel, Field #SQL Model inherits from pydantic models

class TripInput(SQLModel):
    start: int
    end: int
    description: str

class TripOutput(TripInput):
    id:int


class CarInput(SQLModel): #Pydantic makes sure to parse all items into the types specified
    size: str
    fuel: str|None = "electric" #Default values
    doors: int
    transmission: str|None = "auto"
# pydantic methods can be accesed as:
# c.json() or c.dict()
    class Config: #This provide example documentation for tools like postman
        schema_extra = {
            "example" : {
                "size": "m",
                "doors": 5,
                "transmission": "manual",
                "fuel":"hybrid"
            }
        }


class Car(CarInput, table=True): #Tells SQL model that we want to have a database for this model
    id: int | None = Field(primary_key=True, default=None)

class CarOutput(CarInput):
    id:int
    trips: list[TripOutput] = [] #Adding nested model

def load_db() -> list[CarOutput]:
    """Load a list of Car objects from a JSON file"""
    with open ("cars.json") as f:
        return [CarOutput.parse_obj(obj) for obj in json.load(f)]

def save_db(cars: list[CarOutput]):
    with open("cars.json", "w") as f:
        json.dump([car.dict() for car in cars], f, indent=4)