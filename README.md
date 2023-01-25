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

The content of this repo has been organized following the structure that was given on the course. Below links will point you to the specific branches were each topic was covered. Inside each branch, you can also find the subtopics as commits:

- [Basic implementation](https://github.com/martomor/fastapi_fundamentals/tree/basic_implementation)
- [Serving data](https://github.com/martomor/fastapi_fundamentals/tree/serving_data)
  - [Adding Parameters](https://github.com/martomor/fastapi_fundamentals/commit/bbfa5b93d0f0b7951f2369b4cb0df0d0f4fa11d2)
  - [Get operation to return all cars from a list](https://github.com/martomor/fastapi_fundamentals/commit/0abddd3b0febc26807460988ff4dee3fd576d72b)
  - [Add an optional query parameter to filter by size](https://github.com/martomor/fastapi_fundamentals/commit/b2567b0e9fa58d4615e3db63b5a730e51eed9872)
  - [Add typed optional parameters](https://github.com/martomor/fastapi_fundamentals/commit/3997c30cf51b34630596f989b54ec7e4cf46b5f5)
  - [Adding path parameters](https://github.com/martomor/fastapi_fundamentals/commit/a99ba71a9d31e00ee5f585f6aeab5b0f4acc404f)
  - [Return http exceptions 404](https://github.com/martomor/fastapi_fundamentals/commit/7a5baaaf91480712d011cef47501f8b45fd31493)
- [Serving structured data usng PyDantic](https://github.com/martomor/fastapi_fundamentals/tree/serving_with_pydantic_models)
- [Using databases with fastapi](https://github.com/martomor/fastapi_fundamentals/tree/database_with_fastapi)
- [Working with HTTP](https://github.com/martomor/fastapi_fundamentals/tree/http_and_fastapi)
- [Authentication](https://github.com/martomor/fastapi_fundamentals/tree/adding_authentication)
- [Testin and deployment](https://github.com/martomor/fastapi_fundamentals/tree/testing_and_deployment)
- [Docker](https://github.com/martomor/fastapi_fundamentals/tree/docker)

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
