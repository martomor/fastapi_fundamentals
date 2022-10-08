from pydantic import BaseModel

class Car(BaseModel): #Pydantic makes sure to parse all items into the types specified
    id: int
    size: str
    fuel: str|None = "electric" #Default values
    doors: int
    transmission: str|None = "auto"
# pydantic methods can be accesed as:
# c.json() or c.dict()