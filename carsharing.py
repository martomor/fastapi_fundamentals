from fastapi import FastAPI

app = FastAPI()

db = [
     {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
     {"id": 2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
     {"id": 3, "size": "s", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
     {"id": 4, "size": "m", "fuel": "electric", "doors": 3, "transmission": "auto"},
     {"id": 5, "size": "m", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
     {"id": 6, "size": "m", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
     {"id": 7, "size": "l", "fuel": "diesel", "doors": 5, "transmission": "manual"},
     {"id": 8, "size": "l", "fuel": "electric", "doors": 5, "transmission": "auto"},
     {"id": 9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"}
 ]

@app.get("/")
def welcome(name):
    """Return a friendly welcome message"""
    return {'message': f"Welcome {name}, to the car sharing service"}

#You can make a request like this: http://127.0.0.1:8000/?name=Martin

@app.get("/api/cars")
def get_cars():
    """Return all cars"""
    return db