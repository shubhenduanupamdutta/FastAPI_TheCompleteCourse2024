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