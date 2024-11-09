# Databases

---

## Production Database Management System (DBMS) Vs SQLite

---

### SQLite3

- **SQLite3 strives to provide local data storage for individual application and devices.**
- **SQLite3 emphasizes economy, efficiency, reliability, independence, and simplicity.**
- **For most small/medium applications, SQLite3 works perfectly.**
- **SQLite3 focuses on different concepts than a production DBMS.**

### Production Database Management System (DBMS)

- **MySQL, PostgreSQL focuses on a big differences compared to SQLite3.**
- **These production DBMS focuses on scalability, concurrency and control.** They can grow more efficiently and typically offer better scalability than SQLite3.

### When to use SQLite3 and when to use a Production DBMS?

- **If your application is going to have 10s of thousands of users, it may be wise to switch to a production DBMS.**
- **If your application is only you, and a few others, SQLite3 is perfect and will work great.**
- **If your app begins to get huge momentum, you can always scale your application into using a production DBMS.**

---

## Production DBMS Key Notes

---

- **SQLite3 runs in-memory or local disk, which allows development of a SQLite3 database to be easy, as it is part of your application.**
- **Production DBMS run on their own server and port. Which means you need to make sure the database is running, and have authentication linking to the DBMS.**
- **_(SQLite3)_ For deployment you can deploy a SQLite3 database along with the application.**
- **_(Prod DBMS)_ For deployment you will need to also deploy the database separate from the application.**

---

## Overview of Section (For both MySQL & PostgreSQL)

---

### We will, in this section,

- **Go over two production DBMS: MySQL and PostgreSQL.**
- **Learn how to install MySQL and PostgreSQL.**
- **Setup the tables and data within the production DBMS.**
- **Connect FastAPI to the production DBMS.**
- **Learn how to use the production DBMS with FastAPI, i.e. CRUD Operations.**
