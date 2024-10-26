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
