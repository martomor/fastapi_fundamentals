from fastapi import APIRouter
from starlette.responses import HTMLResponse #Library used to serve http

router = APIRouter()

@router.get("/", response_class=HTMLResponse) # so that we dont response json
def home():
    return """
    <html>
        <head>
            <title>Carsharing Demo</title>
        </head>
        <body>
            <h1>Welcome to the Car Sharing service</h1>
            <p>Here is some text for you </p>
        </body>
    </html>
    """