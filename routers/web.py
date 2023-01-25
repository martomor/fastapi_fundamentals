from fastapi import APIRouter, Request, Form, Depends, Cookie
from sqlmodel import Session
from starlette.responses import HTMLResponse #Library used to serve http
from fastapi.templating import Jinja2Templates #For serving HTML files

from db import get_session
from routers.cars import get_cars

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse) # so that we dont response json
def home(request: Request, cars_cookie: str|None = Cookie(None)):
    print(cars_cookie) # Printing the cookie, we could run something if the users has visited us before
    return templates.TemplateResponse("home.html", #Will read the home.html file and return the proper response
                                     {"request": request}) #This is mandatory

@router.post("/search", response_class=HTMLResponse)
def search(*, size: str = Form(...), doors: int = Form(...), #after the * everything becomes a key argument
           request: Request,
           session: Session = Depends(get_session)):
    cars = get_cars(size=size, doors=doors, session=session)
    return templates.TemplateResponse("search_results.html",
                                     {"request": request, "cars":cars})