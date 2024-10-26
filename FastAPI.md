# FastAPI

---

## FastAPI Overview

---

### What is FastAPI?

_**FastAPI** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints._

**Fast** in FastAPI is not just a name, it has double meaning:

- **Fast in Performance**: _It is one of the fastest web frameworks available which is based on Starlette for the web parts and Pydantic for the data parts. It includes data validation, serialization, and documentation and more._
- **Fast to Code**: _FastAPI is designed to be easy to use and easy to learn. It is designed to be simple and intuitive to use, while still providing powerful features. FastAPI makes it super easy to create a backend communication that has embedded security, lightweight installation and can be running within minutes._

---

### Key Notes

---

- #### Few Bugs - _FastAPI allows you to develop APIs with fewer bugs with all the data validation that is embedded. You can see reduction of about 40% of human error and bugs._
- #### Quick & Easy - _FastAPI is designed to be quick and easy to use. It is designed to be simple and intuitive to use, while still providing powerful features._
- #### Robust - _With FastAPI you can get production ready code in minutes, with automatic and dynamic documentation._
- #### Standards - _FastAPI uses OpenAPI standards and JSON Schema._

---

## HTTP Request Methods

---

| **CRUD** | **HTTP Methods** |
| -------- | ---------------- |
| Create   | POST             |
| Read     | GET              |
| Update   | PUT              |
| Delete   | DELETE           |

---

## Path Parameters

---

### What are Path Parameters?

- **Path Parameters are request parameters that are part of the URL path.**
- **Path Parameters are usually defined as a way to find information based on location.**
- **Think of computer file system: You can identify the specific resource based on the file you are in.**

---

### Dynamic Path Parameters

---

- **Dynamic Path Parameters are used to pass data to the server.**
- **Dynamic Path Parameters are defined by the curly braces `{}`.**

```python
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

- **In the above example, `item_id` is a dynamic path parameter.**

#### NOTE: Order of the path parameters is important.

```python
@app.get("/users/{user_id}")
async def read_user_me(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
```

**In the above example, `read_user_me` will never be called because the path `/users/me` will be matched by the first path. This is because FastAPI will always try to match the path in the order they are defined, from top to bottom.**

---

## Query Parameters

---

### What are Query Parameters?

- **Query Parameters are request parameters that have been attached to the URL after `?` character.**
- **Query Parameters have `name=value` pairs.**
- **Example:** `http://127.0.0.1:8000/books/?category=math`
  - In the above example, `category` is the query parameter and `math` is the value.

---

## POST HTTP Request Method

---

### What is the POST Request Method?

- **Used to create data.**
- **Post can have a body that has additional information, that get request do not have.**
- **Example of Body:**
  ```json
  {
    "title": "Concepts of Physics",
    "author": "H.C. Verma",
    "category": "Physics"
  }
  ```
- **In the above example, `title`, `author` and `category` are the keys and `Concepts of Physics`, `H.C. Verma` and `Physics` are the values. the body is in JSON format. And the whole thing can be passed to the server using the POST request method.**

---

## PUT HTTP Request Method

---

### What is the PUT Request Method?

- **Used to update data.**
- **Put can have a body that has additional information (like POST) that GET does not have.**
- **Example of Body:**
  ```json
  {
    "title": "Concepts of Physics",
    "author": "H.C. Verma",
    "category": "Science"
  }
  ```
- **In the above example, `title`, `author` and `category` are the keys and `Concepts of Physics`, `H.C. Verma` and `Science` are the values. The body is in JSON format. And the whole thing can be passed to the server using the PUT request method.**

---

## DELETE HTTP Request Method

---

### What is the DELETE Request Method?

- **Used to delete data.**
- **Delete does not have a body.**
- **Usually a DELETE request will have a path parameter to identify the resource that needs to be deleted.**

---

## Pydantic

---

### What is Pydantic?

- **Pydantic is a python library that is used for data modelling, data parsing and has efficient error handling.**
- **Pydantic is commonly used as a resource for data validation and how to handle data coming to our FastAPI application.**

---

### Implementing Pydantic in FastAPI

---

- **Create a Pydantic model class that will define the structure of the data that will be passed to the FastAPI application, for data validation.**
- **Field data validation on each variable/element in the Pydantic model class.**
- **This new model will be inherit from the Pydantic BaseModel class.**

```python
from pydantic import BaseModel

class Book(BaseModel):
    title: str
```

**In the above example, we have created a Pydantic model class called `Book` that has a single field called `title` which is of type `str`. This will validate that the data passed to the FastAPI application has a `title` key and the value is a string.**

---

## Status Codes

---
### What are Status Codes?
- **An HTTP Status Code is used to help the client (the user or system submitting the data to the server) to understand what happened on the server side application.**
- **Status Codes are three digit numbers, and are international standard on how a Client/Server should handle the result of the request.**
- **It allows everyone to understand what happened, whether their request was successful or not.**

---
### Most Common Status Codes
- **1xx**: Informational Response -> Request received, continuing process ...etc.
- **2xx**: Success -> The action was successfully received, understood, and accepted.
- **3xx**: Redirection -> Further action must be taken in order to complete the request.
- **4xx**: Client Error -> The request contains bad syntax or cannot be fulfilled.
- **5xx**: Server Error -> The server failed to fulfill an apparently valid request.

---
### 2xx Success Status Codes
- **200 OK**: Standard response for successful HTTP requests. Commonly used for successful GET requests when data is being returned.
- **201 Created**: The request has been fulfilled, resulting in the creation of a new resource by POST requests.
- **204 No Content**: The server has successfully fulfilled the request and that there is no additional content to send in the response payload body, commonly used with PUT and DELETE requests.

---
### 4xx Client Error Status Codes
- **400 Bad Request**: The server cannot or will not process the request due to an apparent client error. Commonly used for invalid data in the request.
- **401 Unauthorized**: Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided.
- **403 Forbidden**: The request was valid, but the server is refusing action. The user might not have the necessary permissions for a resource, or may need an account of some sort.
- **404 Not Found**: The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.
- **405 Method Not Allowed**: A request method is not supported for the requested resource; for example, a GET request on a form that requires data to be presented via POST, or a PUT request on a read-only resource.
- **422 Unprocessable Entity**: The request was well-formed but was unable to be followed due to semantic errors.

---
### 5xx Server Error Status Codes
- **500 Internal Server Error**: A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.
- **502 Bad Gateway**: The server was acting as a gateway or proxy and received an invalid response from the upstream server.
- **503 Service Unavailable**: The server cannot handle the request (because it is overloaded or down for maintenance). Generally, this is a temporary state.
