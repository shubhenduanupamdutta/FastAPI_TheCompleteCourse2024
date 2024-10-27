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