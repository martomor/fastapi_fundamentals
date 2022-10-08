from fastapi import FastAPI, HTTPException
import uvicorn

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
def get_cars(size:str|None, doors:int|None) -> list: #size:str|None means that we accept str or none values
# def get_cars(size:Optional[str] = None, doors:Optional[str] = None) -> List: for python < 3.10 
    """Return all car or filter by size or number of doors """
    result = db
    if size:
        result = [car for car in result if car['size'] == size]
    if doors:
        result = [car for car in result if car['doors'] == doors]
    return result

#You can make a request like this: http://127.0.0.1:8000/api/cars?size=s&doors=3

@app.get("/api/cars/{id}") #Path parameter - This creates a unique url for each car
def car_by_id(id: int) -> dict:
    """Returns the information of a car by id"""
    result = [car for car in db if car['id'] == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
#You can make a request like this: http://127.0.0.1:8000/api/cars/1

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)