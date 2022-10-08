from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome(name):
    """Return a friendly welcome message"""
    return {'message': f"Welcome {name}, to the car sharing service"}

#You can make a request like this: http://127.0.0.1:8000/?name=Martin