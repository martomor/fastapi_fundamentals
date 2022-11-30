from fastapi import FastAPI, Request
import uvicorn
from sqlmodel import SQLModel
from routers import cars, web
from routers.cars import BadTripException
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from db import engine


app = FastAPI(title="Car Sharing")
app.include_router(cars.router)
app.include_router(web.router)

@app.on_event("startup") # On startup will be loaded after all the code has been declared
def on_startup():
    SQLModel.metadata.create_all(engine) #Creates the database at start event

@app.exception_handler(BadTripException) # Status Codes and Error Handling
async def unicorn_exception_handler(request: Request, exc:BadTripException):
    return JSONResponse(
        status_code = HTTP_422_UNPROCESSABLE_ENTITY,
        current = {"message" : "Bad Trip"},
    )

@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie", value = "you_visited_the_carsharing_app")
    return response
    
if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)