from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse #Library used to serve http
from fastapi.templating import Jinja2Templates #For serving HTML files

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse) # so that we dont response json
def home(request: Request):
    return templates.TemplateResponse("home.html", #Will read the home.html file and return the proper response
                                     {"request": request}) #This is mandatory