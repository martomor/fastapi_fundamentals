from fastapi import Depends, FastAPI, HTTPException
import uvicorn

from sqlmodel import SQLModel, Session, create_engine, select

from schemas import Car, CarInput, CarOutput, Trip, TripInput, TripOutput

app = FastAPI(title="Car Sharing")


engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False}, #Needed for SQlite and FastAPI
    echo=True #Log generated SQL - Not for prod
)

@app.on_event("startup") # On startup will be loaded after all the code has been declared
def on_startup():
    SQLModel.metadata.create_all(engine) #Creates the database at start event
    
def get_session():
    with Session(engine) as session:
        yield session #The with session will be closed as soon as the get_session execution is finished. This wraps everything inside the tiwh block. If anything goes wrong, it will revert the entire operation.


@app.get("/api/cars")
def get_cars(size:str|None = None, doors:int|None = None,
            session: Session = Depends(get_session)) -> list: # We are not calling the function, we are passing it as a value to depends. 
    """Return all car or filter by size or number of doors """
    query = select(Car)
    if size:
        query = query.where(Car.size == size)
    if doors:
        query = query.where(Car.doors >= doors)
    return session.exec(query).all()

#You can make a request like this: http://127.0.0.1:8000/api/cars?size=s&doors=3

@app.get("/api/cars/{id}", response_model=CarOutput) #Path parameter - This creates a unique url for each car. CarOutput model will include the trips relations, Car will not
def car_by_id(id: int, session: Session = Depends(get_session)) -> Car:
    """Returns the information of a car by id"""
    car = session.get(Car, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
#You can make a request like this: http://127.0.0.1:8000/api/cars/1

@app.post("/api/cars", response_model=Car) #Post operation, cannot be called as an url. Including the response model to specify and validate the output as a CarOutput or Car
def add_car(car_input:CarInput, session: Session = Depends(get_session)) -> Car:
    new_car = Car.from_orm(car_input)
    session.add(new_car)
    session.commit()
    session.refresh(new_car) #We refresh to get the id
    return new_car


@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id:int, session: Session = Depends(get_session)) -> None:
    car = session.get(Car, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")

@app.put("/api/cars/{id}", response_model=Car) #Example of having a path parameters and an input body
def change_car(id: int, new_data: CarInput,
               session: Session = Depends(get_session)) -> Car:
    car = session.get(Car, id)
    if car:
        car.fuel = new_data.fuel
        car.transmission = new_data.transmission
        car.size = new_data.size
        car.doors = new_data.doors
        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")

@app.post("/api/cars/{car_id}/trips", response_model=Trip)
def add_trip(car_id: int, trip_input: TripInput,
             session: Session = Depends(get_session)) -> Trip:
    car = session.get(Car, car_id)
    if car:
        new_trip = Trip.from_orm(trip_input, update={'car_id': car_id})
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
        
if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)