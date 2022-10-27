from fastapi import FastAPI, HTTPException
import uvicorn

from schemas import CarInput, CarOutput, load_db, save_db

app = FastAPI()

db = load_db()


@app.get("/api/cars")
def get_cars(size:str|None = None, doors:int|None = None) -> list: #size:str|None means that we accept str or none values
# def get_cars(size:Optional[str] = None, doors:Optional[str] = None) -> List: for python < 3.10 
    """Return all car or filter by size or number of doors """
    result = db
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors == doors]
    return result

#You can make a request like this: http://127.0.0.1:8000/api/cars?size=s&doors=3

@app.get("/api/cars/{id}") #Path parameter - This creates a unique url for each car
def car_by_id(id: int) -> dict:
    """Returns the information of a car by id"""
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
#You can make a request like this: http://127.0.0.1:8000/api/cars/1

@app.post("/api/cars", response_model=CarOutput) #Post operation, cannot be called as an url. Including the response model to specify and validate the output as a CarOutput
def add_car(car:CarInput) -> CarOutput:
    new_car = CarOutput(size=car.size, doors=car.doors,
                        fuel=car.fuel, transmission=car.transmission,
                        id=len(db)+1)
    db.append(new_car)
    save_db(db)
    return new_car

if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)