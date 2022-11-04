from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel
from routers import cars

from db import engine


app = FastAPI(title="Car Sharing")
app.include_router(cars.router)

@app.on_event("startup") # On startup will be loaded after all the code has been declared
def on_startup():
    SQLModel.metadata.create_all(engine) #Creates the database at start event
    
if __name__ == "__main__":
    uvicorn.run("carsharing:app", reload=True)