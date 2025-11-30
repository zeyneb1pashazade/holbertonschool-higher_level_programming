# **SQL – More Queries**

This directory covers more advanced SQL topics, including data access permissions, advanced queries, JOIN operations, subqueries, and database objects. The goal is to strengthen your understanding of how real database systems work.

---

## **Topics Covered**

### **1. DCL (Data Control Language)**

Used to manage access rights and permissions in a database.

Main commands:

* `GRANT` – gives a user permission
* `REVOKE` – removes a permission

Common privileges:

* `SELECT` – read-only access
* `INSERT` – insert rows
* `UPDATE` – update rows
* `DELETE` – delete rows
* `ALL PRIVILEGES` – full access

---

### **2. Database and Table Permissions**

A user can be granted specific access levels:

* Read-only access to a database
* Read-only access to a table
* Insert-only / Delete-only / Update-only access
* Permissions to multiple tables or databases

Example:

```sql
GRANT SELECT ON database_name.table_name TO 'user'@'localhost';
```

---

### **3. JOIN Types**

JOINs are used to combine rows from multiple tables based on a related column.

Valid JOIN types:

* **INNER JOIN** – returns matching rows only
* **LEFT JOIN** – all rows from the left table
* **RIGHT JOIN** – all rows from the right table
* **FULL OUTER JOIN** (depends on SQL engine) – all rows from both tables

Invalid / non-existent JOIN types:

* IN LEFT
* RIGHT AND LEFT
* TOP
* FULL INNER

---

### **4. Subqueries**

A subquery is a query inside another query.

Used in:

* `WHERE` clause
* `FROM` clause (as a temporary table)
* `SELECT` clause

Example:

```sql
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders);
```

---

### **5. Views**

A view is a stored SQL query that behaves like a virtual table.

Creating a view:

```sql
CREATE VIEW view_name AS
SELECT column1, column2 FROM table_name;
```

---

### **6. Constraints**

Constraints ensure data accuracy and integrity.

Main types:

* PRIMARY KEY
* FOREIGN KEY
* UNIQUE
* NOT NULL
* DEFAULT
* CHECK

---

## **Directory Structure**

```
SQL_more_queries/
│
├── 0-privileges.sql
├── 1-create_user.sql
├── 2-give_permissions.sql
├── 3-revoke_permissions.sql
├── 4-join_queries.sql
├── 5-subqueries.sql
├── 6-create_view.sql
└── README.md   ← this file
```

---

## **Summary**

