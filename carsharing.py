from fastapi import FastAPI, HTTPException
from requests import session
import uvicorn

from sqlmodel import SQLModel, Session, create_engine, select

from schemas import Car, CarInput, CarOutput, TripInput, TripOutput, load_db, save_db

app = FastAPI(title="Car Sharing")

db = load_db()

engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False}, #Needed for SQlite and FastAPI
    echo=True #Log generated SQL - Not for prod
)

@app.on_event("startup") # On startup will be loaded after all the code has been declared
def on_startup():
    SQLModel.metadata.create_all(engine) #Creates the database at start event
    


@app.get("/api/cars")
def get_cars(size:str|None = None, doors:int|None = None) -> list: #size:str|None means that we accept str or none values
# def get_cars(size:Optional[str] = None, doors:Optional[str] = None) -> List: for python < 3.10 
    """Return all car or filter by size or number of doors """
    with Session(engine) as session: #Creates an SQL query 
        query = select(Car)
        if size:
            query = query.where(Car.size == size)
        if doors:
            query = query.where(Car.doors >= doors)
        return session.exec(query).all()

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

@app.post("/api/cars", response_model=Car) #Post operation, cannot be called as an url. Including the response model to specify and validate the output as a CarOutput or Car
def add_car(car_input:CarInput) -> Car:
    with Session(engine) as session: #Database transaction, it will only be executed if everything works
        new_car = Car.from_orm(car_input)
        session.add(new_car)
        session.commit()
        session.refresh(new_car) #We refresh to get the id
        return new_car


@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id:int ) -> None:
    matches = [car for car in db if car.id==id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_db(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")

@app.put("/api/cars/{id}", response_model=CarOutput) #Example of having a path parameters and an input body
def change_car(id: int, new_data: CarInput) -> CarOutput:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        car.fuel =  new_data.fuel
        car.transmission = new_data.transmission
        car.size = new_data.size
        car.doors = new_data.doors
        save_db(db)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")

@app.post("/api/cars/{car_id}/trips", response_model=TripOutput)
def add_trip(car_id:int, trip:TripInput) -> TripOutput:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        new_trip = TripOutput(id=len(car.trips)+1,
                              start=trip.start, end=trip.end,
                              description=trip.description)
        car.trips.append(new_trip)
        save_db(db)
        return new_trip

    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
        
if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)