from schemas import Car, CarInput, CarOutput, Trip, TripInput
from db import get_session
from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select
#from carsharing import app -> This creates a circular import thats why we need API router

router = APIRouter(prefix="/api/cars") # It will this url prefix for all operations on the router

@router.get("/")
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

@router.get("/{id}", response_model=CarOutput) #Path parameter - This creates a unique url for each car. CarOutput model will include the trips relations, Car will not
def car_by_id(id: int, session: Session = Depends(get_session)) -> Car:
    """Returns the information of a car by id"""
    car = session.get(Car, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
#You can make a request like this: http://127.0.0.1:8000/api/cars/1

@router.post("/", response_model=Car) #Post operation, cannot be called as an url. Including the response model to specify and validate the output as a CarOutput or Car
def add_car(car_input:CarInput, session: Session = Depends(get_session)) -> Car:
    new_car = Car.from_orm(car_input)
    session.add(new_car)
    session.commit()
    session.refresh(new_car) #We refresh to get the id
    return new_car


@router.delete("/{id}", status_code=204)
def remove_car(id:int, session: Session = Depends(get_session)) -> None:
    car = session.get(Car, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")

@router.put("/{id}", response_model=Car) #Example of having a path parameters and an input body
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

@router.post("/{car_id}/trips", response_model=Trip)
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
        