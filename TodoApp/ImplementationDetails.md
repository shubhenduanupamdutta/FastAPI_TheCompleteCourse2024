# TODOs Implementation Details

---

## Creating a TODO Table

---

- **We will create new Todo Table Models for our application.**
- **We will using these ToDos to save records throughout this project.**
- **We will also create a new database for our application.**
- **Now our projects is said to be divided into three parts**
  - **Web Page**
  - **Server (FastAPI)**
  - **Database**
- **Frontend (Web Page) communicates with the Server (FastAPI). FastAPI server handles authorization, authentication, and CRUD operations.**
- **FastAPI server communicates with the Database to perform CRUD operations i.e. retrieve, update, delete, and create records in the database of users and todos.**

---

## Database

---

### What is database?

- **Organized collection of structured information of **data**, which is stored in a computer system.**
- **The data can be easily accessed**
- **The data can be easily modified**
- **The data can be controlled and organized**
- **Many databases use a structured query language (SQL) to modify and write data.**
- **A database is a collection of data.**
- **Since data, on its own, is just data. A database allows management of data.**
- **Databases are organized in how data can be retrieved, stored and modified.**
- **There are many types of _Database Management Systems (DBMS)_. It is a software that allows users to interact with databases.**
- **Some of the popular DBMS are:**
  - **MySQL**
  - **PostgreSQL**
  - **SQLite**
  - **Oracle**
  - **Microsoft SQL Server**

---

### What is Data?

- Data can be related to just about any object.
- For example, a user on an application may have:
  - Name
  - Age
  - Email
  - Password
- All four of the characteristics of User (Name, Age, Email, Password) are data.

---

### What is SQL?

- _Pronounced as "S-Q-L" or "sequel"_
- _Standard language for dealing with relational databases._
- _SQL can be used to different things with database records._
  - _Create new records_
  - _Read records_
  - _Update records_
  - _Delete records_

---

### What is SQLAlchemy?

- **SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python.**
- **It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.**

---

### Basic SQL Queries

#### Inserting Database Table

```sql
INSERT INTO todos (title, description, priority, complete)
VALUES ('Go to store', 'To pick up eggs', 4, False);

INSERT INTO todos (title, description, priority, complete)
VALUES ('Haircut', 'Need to get length 1mm', 3, False);
```

#### Reading Data - SELECT SQL Query

```sql
SELECT * FROM todos;
```

_Will return all the records from the todo table_

```sql
SELECT title FROM todos;
```

_Will return only the title column from the todo table_

```sql
SELECT description FROM todos
```

_Will return only the description column from the todo table_

```sql
SELECT title, description FROM todos;
```

_Will return title and description columns from the todo table_

#### WHERE Clause

_Will return all the records from the the condition is met_

```sql
SELECT * FROM todos WHERE priority = 4;
```

_Will return all the records from the todo table where the priority is 4_

```sql
SELECT * FROM todos WHERE title='Feed Dog'
```

- _Will return all the records from the todo table where the title is 'Feed Dog'_

```sql
SELECT * FROM todos WHERE id=2
```

- _Will return all the records from the todo table where the id is 2_

#### Update Clause - UPDATE SQL Query

```sql
UPDATE todos SET complete = True WHERE id = 5;
```

- _Will update the complete column to True where the id is 5_

```sql
UPDATE todos set complete=True WHERE title='Learn Something new';
```

- _Will update the complete column to True where the title is 'Learn Something new'. This will update all the records where the title is 'Learn Something new'_

#### Delete Clause - DELETE SQL Query

```sql
DELETE FROM todos WHERE id = 5;
```

- _Will delete the record from the todo table where the id is 5_

```sql
DELETE FROM todos WHERE title='Learn Something new';
```

- _Will delete the record from the todo table where the title is 'Learn Something new'. This will delete all the records where the title is 'Learn Something new'_

---

### Opening and Working with SQLite Database using command line

#### Connecting to SQLite Database

- **Move to the directory where the database is stored**
- **Open the SQLite database using the command line**

```
sqlite <database name>
```

- In our case, the database name is `todos.db`

```sql
sqlite todos.db
```

- **This will open the SQLite database, todo.db**
- **Now we can run the SQL queries to perform CRUD operations**

#### Inserting one row into the database

```sql
insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False);
```

```sql
select * from todos;
```

We get the output as:

```
1|Go to the store|Pick up eggs|5|0
```

**Id is auto generated, since we have set it as primary key**

#### Changing the output format from SQLite

```sql
.mode column
```

```bash
id  title            description            priority  complete
--  ---------------  ---------------------  --------  --------
1   Go to the store  Pick up eggs           5         0
2   Cut the lawn     Grass is getting long  3         0
3   Feed the dog     He is getting hunbgry  5         0
```

```sql
.mode markdown
```

```bash
| id |      title      |      description      | priority | complete |
|----|-----------------|-----------------------|----------|----------|
| 1  | Go to the store | Pick up eggs          | 5        | 0        |
| 2  | Cut the lawn    | Grass is getting long | 3        | 0        |
| 3  | Feed the dog    | He is getting hunbgry | 5        | 0        |
```

```sql
.mode box
```

```bash
┌────┬─────────────────┬───────────────────────┬──────────┬──────────┐
│ id │      title      │      description      │ priority │ complete │
├────┼─────────────────┼───────────────────────┼──────────┼──────────┤
│ 1  │ Go to the store │ Pick up eggs          │ 5        │ 0        │
│ 2  │ Cut the lawn    │ Grass is getting long │ 3        │ 0        │
│ 3  │ Feed the dog    │ He is getting hunbgry │ 5        │ 0        │
└────┴─────────────────┴───────────────────────┴──────────┴──────────┘
```

```sql
.mode table
```

```bash
+----+-----------------+-----------------------+----------+----------+
| id |      title      |      description      | priority | complete |
+----+-----------------+-----------------------+----------+----------+
| 1  | Go to the store | Pick up eggs          | 5        | 0        |
| 2  | Cut the lawn    | Grass is getting long | 3        | 0        |
| 3  | Feed the dog    | He is getting hunbgry | 5        | 0        |
+----+-----------------+-----------------------+----------+----------+
```

#### Deleting a row from the database

**Current Status of database table**

```bash
┌────┬─────────────────┬───────────────────────┬──────────┬──────────┐
│ id │      title      │      description      │ priority │ complete │
├────┼─────────────────┼───────────────────────┼──────────┼──────────┤
│ 1  │ Go to the store │ Pick up eggs          │ 5        │ 0        │
│ 2  │ Cut the lawn    │ Grass is getting long │ 3        │ 0        │
│ 3  │ Feed the dog    │ He is getting hunbgry │ 5        │ 0        │
│ 4  │ Test element    │ He is getting hungry  │ 5        │ 0        │
└────┴─────────────────┴───────────────────────┴──────────┴──────────┘
```

**Deleting the row with id 4**

```sql
delete from todos where id=4;
```

**Now the table looks like**

```bash
┌────┬─────────────────┬───────────────────────┬──────────┬──────────┐
│ id │      title      │      description      │ priority │ complete │
├────┼─────────────────┼───────────────────────┼──────────┼──────────┤
│ 1  │ Go to the store │ Pick up eggs          │ 5        │ 0        │
│ 2  │ Cut the lawn    │ Grass is getting long │ 3        │ 0        │
│ 3  │ Feed the dog    │ He is getting hunbgry │ 5        │ 0        │
└────┴─────────────────┴───────────────────────┴──────────┴──────────┘
```

---

### Using SQLAlchemy to perform CRUD operations

- **Getting all the records from the database**

```python
db.query(Todo).all()
```

- **Getting one record from the database**

```python
db.query(Todo).filter_by(Todo.id == 1).first()
```

_This will return the first record where the id is 1. `first()` is used to get the first record from the query result, this optimizes the query and tells to return as soon as you get the first record, and don't look for more records._

---

## One to Many Relationship

---

_**One to Many Relationship** is a type of relationship where a single record in one table can be related to multiple records in another table. For example, a single user can have multiple todos. This is a one to many relationship._

- **In our case, a single user can have multiple todos.**
- **We will create a one to many relationship between the User and Todo table.**
- **We will create a new table User and add a foreign key to the Todo table.**

---

## Foreign Key (FK)

---

### What is Foreign Key?

- **A foreign key (FK) is a column within a relational database table that provides a link between data in two tables.**
- **A foreign key references a primary key in another table.**
- **Most relational databases require a foreign key to be defined in a table, to link the table with another table.**

---

### Query to use foreign key

```sql
SELECT * FROM todos
```

**Above query will return all the records from the todos table**

```sql
SELECT * FROM users
```

**Above query will return all the records from the users table**

```sql
SELECT * FROM todos WHERE owner = 1;
```

**This query will get all todos where owners primary key is 1**

---

## JSON Web Tokens (JWT)

---

### What is JSON Web Token (JWT)?

- **JSON Web token (JWT) is a self-contained way to securely transmit data and information between two parties using a JSON Object.**
- **JWT can be trusted because each JWT can be digitally signed, which in return allows the server to know if the JWT has been changed at all.**
- **JWT is not an authentication method like basic and digest, but an authorization method, which allows the client and server to maintain a relationship without having to log in every time.**
- **JWT is a great way for information to be exchanged between the server and client. Once a user logs in, the server will return a JWT, which is a string of character that, when decoded, shows information about the client and user. Each time a request comes from the same client, after a successful authentication, the client will send the JWT and the server will validate the JWT and allow the client to access the resources.**

---

### JSON Web Token Structure

---

```bash
aaaaaaaaaaa.bbbbbbbbbbbbbb.ccccccccccccc
```

- **A JWT is created of three separate parts separated by dots(.) which include:**
  - **Header (a)**
  - **Payload (b)**
  - **Signature (c)**
- **JWT Header**

  - _A JWT header usually consist of two parts:_

    ```json
    {
      "alg": "HS256",
      "typ": "JWT"
    }
    ```

    - (alg) The algorithm for signing
    - (typ) The type of token

  - _The JWT header is then encoded using Base64 to create the first part of the JWT (a)_

- **JWT Payload**
  - _A JWT Payload consists of the data. The payloads data contains claims, and there are three different types of claims:_
    - Registered Claims
    - Public Claims
    - Private Claims
  ```json
  {
    "sub": "1234567890",
    "name": "John Doe",
    "given_name": "John",
    "family_name": "Doe",
    "email": "shubh@gmail.co.in",
    "admin": true
  }
  ```
  - _Registered Claims are claims that are predefined, recommended but not mandatory. Top 3 registered claims are:_
    - **iss** (Issuer) - This identifies the principal that issued the JWT
    - **sub** (Subject) - Holds statement about the subject of the JWT. The subject must be scoped either globally or locally unique. Think of subject as a unique identifier for JWT.
    - **exp** (Expiration Time) - This claim makes sure that the current date and time is before the expiration date and time specified in the claim. It is not mandatory but recommended, and extremely useful. If the JWT never expires, then anyone who has the JWT can access the resources, which is not good.
  - _Public Claims are claims that are defined by the JWT standard. These claims are not mandatory but recommended. Some of the public claims are:_
    - **name** - Name of the user
    - **admin** - If the user is an admin or not
    - **email** - Email of the user
  - _Private Claims are claims that are defined by the user. These claims are not mandatory but recommended. Some of the private claims are:_
    - **given_name** - Given name of the user
    - **family_name** - Family name of the user
  - _JWT Payload is then encoded using Base64 to create the second part of the JWT (b)_
- **JWT Signature**
  - _The JWT Signature is created by using the algorithm in the header to hash out the encoded header, encoded payload with a secret._
  - _The secret can be anything, but is saved somewhere on the server that the client doesn't have access to._
  - _The signature is third and final part of the JWT (c)_

### JWT Example

- **JWT Header**
  ```json
  {
    "alg": "HS256",
    "typ": "JWT"
  }
  ```
- **JWT Payload**
  ```json
  {
    "sub": "1234567890",
    "name": "John Doe",
    "given_name": "John",
    "family_name": "Doe",
    "email": "john_doe@gmail.co.in",
    "admin": true
  }
  ```
- **JWT Signature**
  ```text
  HMACSHA256(
      base64UrlEncode(header) + "." +
      base64UrlEncode(payload),
      learn_online
  )
  ```
- **JSON Web Token (JWT)**

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiZ2l2ZW5fbmFtZSI6IkpvaG4iLCJmYW1pbHlfbmFtZSI6IkRvZSIsImVtYWlsIjoiam9obl9kb2VAZ21haWwuY28uaW4iLCJhZG1pbiI6dHJ1ZX0.BuRCSTthQdAY9qmH0lXh1khCyI4_37WITqigxw5qW4M
```

---

### More about JWT

- **We get the JWT as a string, as shown above.**
- **This string is completely unique to the client based on the authentication of the user that has logged in.**
- **When working with JWT, the requester usually sends a token in the authorization header using the bearer schema.**
- **This is a different schema than the basic authentication and digest authentication.**
- **Now with all security measures within APIs, it is important to know that JWT is not a security measure, but a way to authorize the client to access the resources.**
- **JWT Is safe to use until the secret is safe. If the secret is leaked, then the JWT is no longer safe.**

---

### JWT Practical Use Cases

---

- **Imagine this scenario, a single company or enterprise has multiple different application that many users work with.**
- **For example, let's say you want to get into cryptocurrency.**
    - _App One is cryptocurrency market where you can buy and sell many different types of cryptocurrencies._
    - _The same company owns another application, App Two, where you can store cryptocurrency in a digital wallet._
    - _The company will not want the user to sign in every time they switch between the two applications._
    - _It would be a much better experience, if the user didn't even notice that there were two different applications._
    - _This is where JWT comes in. If both App One and App Two share the same secret, then the user can log in once and access both applications without having to log in again._

- **JWT is a specially useful in microservices, where multiple services are working together, and are stateless but will require user information. These microservices can use JWT to authorize the user to access the resources, without having a separate user authentication/authorization endpoint.**

---