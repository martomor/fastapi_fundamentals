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
  - [Creating a Pydantic model](https://github.com/martomor/fastapi_fundamentals/commit/74f041bca71171476c2ca3b2126dac56ca1fd651)
  - [Loading from Json files](https://github.com/martomor/fastapi_fundamentals/commit/cc0d30798e6f85353ecf87d22a61e85e423b0943)
  - [Includig None defaults parameters](https://github.com/martomor/fastapi_fundamentals/commit/8c256a4fbb7620ed4568e1444f786a171c0250b6)
  - [Adding a Post Operation](https://github.com/martomor/fastapi_fundamentals/commit/0c00dfb5760c9f099f91c6790ee5d58ab342d20e)
  - [Implementing input and output models](https://github.com/martomor/fastapi_fundamentals/commit/77795b3d5f482898b5e8b84d370bce28cfd49132)
  - [Implementing a response model](https://github.com/martomor/fastapi_fundamentals/commit/a2c8e9deebcaefca7e37bbea5e39ae682bdf8b27)
  - [Implementation of PUT and DELETE](https://github.com/martomor/fastapi_fundamentals/commit/6c28dbef77f64868c3381d9ad01984e464ccd2ba)
  - [Adding example data for documentation](https://github.com/martomor/fastapi_fundamentals/commit/5534a84873e970b62e2978167eebc5778e18796e)
  - [Nested models](https://github.com/martomor/fastapi_fundamentals/commit/a51e814237d9e49093f13f659fc0127f9a8f4a36)
- [Using databases with fastapi](https://github.com/martomor/fastapi_fundamentals/tree/database_with_fastapi)
  - [Creating a data model](https://github.com/martomor/fastapi_fundamentals/commit/3fca4b55c293ab1c1397d94eaa3103323b02158d)
  - [Creating a database](https://github.com/martomor/fastapi_fundamentals/commit/bfa5234dfbc318a7b36c398850286d049fad59e5)
  - [Inserting a new car](https://github.com/martomor/fastapi_fundamentals/commit/b633c0d6d84e6fdea0ea15e799ee928f412f73a0)
  - [Querying the database](https://github.com/martomor/fastapi_fundamentals/commit/a51a60937f889d174c4fba2939a5335a471f13ff)
  - [Session Injection](https://github.com/martomor/fastapi_fundamentals/commit/d5e846bd5481fd69bcc2c10de30048b3ba35520d)
  - [Implementing get,put and delete with sqlmodel](https://github.com/martomor/fastapi_fundamentals/commit/061015ca83f59dce1c4532369ac36d65e57da32a)
  - [Working with Relations](https://github.com/martomor/fastapi_fundamentals/commit/5663d269ae7d0abe6a0f338ee92cb6c7c5c401ff)
- [Working with HTTP](https://github.com/martomor/fastapi_fundamentals/tree/http_and_fastapi)
  - [Organizing code with apirouters](https://github.com/martomor/fastapi_fundamentals/commit/f5003a247e2fc8d91a563d2b77bc5b218b6971ae)
  - [Serving a Web Page](https://github.com/martomor/fastapi_fundamentals/commit/3e018641e9e4988771a8babbac10aedf678864fa)
  - [Dynamic html with Jinja](https://github.com/martomor/fastapi_fundamentals/commit/22f5ed10f02d861ca95f3631f996eda42eb71fd1)
  - [Processing Form data](https://github.com/martomor/fastapi_fundamentals/commit/ac779c4d4de47fddffd75a612f87ac82ca9816ce)
  - [Status codes and error handling](https://github.com/martomor/fastapi_fundamentals/commit/84fc86b6857943022a540924504b6cd299ffbb76)
  - [Middleware](https://github.com/martomor/fastapi_fundamentals/commit/f9b7f01c394c390c028888fd8d13a18138793361)
  - [Headers and cookies](https://github.com/martomor/fastapi_fundamentals/commit/3c8bd7cdcc268ac579bf11a9b865f3db1f13e6bf)
  - [CORS Middleware](https://github.com/martomor/fastapi_fundamentals/commit/3984756aaa58cd0e7aa1ddbcd5cd2c6ac133ebcc)
- [Authentication](https://github.com/martomor/fastapi_fundamentals/tree/adding_authentication)
  - [Adding a user model](https://github.com/martomor/fastapi_fundamentals/commit/026864a455a27d5bfbd6de1c5ba0f7ca9f5fb971)
  - [Password hashing](https://github.com/martomor/fastapi_fundamentals/commit/3a3d0b974d965d8cfe467234b16f7625453ace24)
  - [Column settings: unique and index](https://github.com/martomor/fastapi_fundamentals/commit/a531b035e02f0767857103ef5796a12e2f08288b)
  - [Http basic authentication](https://github.com/martomor/fastapi_fundamentals/commit/28da69739349b3e9d0ea74f049dfeb2e2c3b3a6f)
  - [OAuth2](https://github.com/martomor/fastapi_fundamentals/commit/687c87c4eaa76430f3f4ed41ed47c75221b574dd)
- [Testing and deployment](https://github.com/martomor/fastapi_fundamentals/tree/testing_and_deployment)
  - [Unit testing](https://github.com/martomor/fastapi_fundamentals/commit/7ab242ccb7e34e34bb3515646eb64a62840b8221)
- [Docker](https://github.com/martomor/fastapi_fundamentals/tree/docker)
  - [adding a docker container](https://github.com/martomor/fastapi_fundamentals/commit/ee692ecf2582439db0fec17f458a910a47f47cad)

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
