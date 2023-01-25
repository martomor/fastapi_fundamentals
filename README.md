# Fast API Implementation
Basic FastAPI implementation from Pluralsight. In this implementation you will find:

- Serving data with Fastapi
- Serving structured data using pydantic models
- Databases and Fastapi
- HTTP with Fastapi
- Authentication: HTTP basic authentication and OAuth2
- Testing
- Docker Deployment (This was not covered in the course)

This repo is based on the work done by Reindert-Jan Ekker on [FastAPI Fundamentals course](https://www.pluralsight.com/courses/fastapi-fundamentals) from Pluralsight.

You can find the original implementation in here: [codesensei-courses/fastapi_fundamentals](https://github.com/codesensei-courses/fastapi_fundamentals) 

# How to use this repository?

### Requirements

Note that you can reproduce this code only with python 3.10 or above. The user and password to authenticate into the api is **martin**

### Local Run

You can create a virtual environment using your package mananger of preference:

```
#create a new virtual environment
python -m venv venv

#activate the enviornment
source venv/bin/activate
```
Install the dependencies:

```
pip install -r requirements.txt
```

Run the below to setup the application:

```
pip install -r requirements.txt
```

The app will be served in this url: http://127.0.0.1:8000 and you can check the documentation in here:http://127.0.0.1:8000/docs

#### Runing Tests

To run the pytests you can simply run this command:

```
python -m pytest 
```

#### Creating New Users

To create new users you can simply run:

```
python create_user.py
```


### Container Run

You can also deploy this api using docker. Just need to run:

```
docker compose up
```

And that´s it!!
