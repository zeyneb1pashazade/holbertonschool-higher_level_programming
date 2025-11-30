# **NoSQL**

This directory covers the basics of NoSQL databases, their characteristics, data models, and how they differ from traditional relational databases. The goal is to understand when and why NoSQL systems are used, and how data is structured in non-relational environments.

---

## **What Is NoSQL?**

**NoSQL (Not Only SQL)** refers to a group of databases designed to handle:

* Large volumes of data
* Unstructured or semi-structured data
* High scalability
* Flexible schemas

Unlike SQL databases, NoSQL does **not** rely on fixed tables with rows and columns.

---

## **Main Types of NoSQL Databases**

### **1. Document Databases**

Store data in **JSON**, **BSON**, or similar document formats.
Example: **MongoDB**

Characteristics:

* Flexible schema
* Nested data
* Good for hierarchical structures

---

### **2. Key-Value Stores**

Data is stored as a simple **key → value** pair.
Example: **Redis**, **Amazon DynamoDB**

Characteristics:

* Very fast
* Used for caching, sessions, and real-time applications

---

### **3. Column-Family Stores**

Data is stored in **columns** instead of rows, optimized for large datasets.
Example: **Apache Cassandra**, **HBase**

Characteristics:

* High scalability
* Efficient for analytical workloads

---

### **4. Graph Databases**

Data is organized as **nodes** and **edges**, ideal for relationship-heavy data.
Example: **Neo4j**

Characteristics:

* Optimized for social networks, recommendations, path finding

---

## **Key Features of NoSQL**

* **Schema-less design** → data structure can change anytime
* **Horizontal scaling** → add more servers to handle more load
* **High availability**
* **Fast read/write operations**
* **Supports big data**

---

## **When to Use NoSQL?**

Use NoSQL when:

* Data is unstructured (text, logs, JSON, etc.)
* The system must scale horizontally
* You need high write throughput
* Flexibility of schema is important
* Relationships are complex (graph databases)

---

## **When NOT to Use NoSQL?**

Avoid NoSQL when:

* Strong ACID transactions are needed
* The data model is highly structured
* Complex JOIN operations are required

---

## **Directory Structure**

```
NoSQL/
│
├── 0-introduction.txt
├── 1-types_of_nosql.txt
├── 2-advantages.txt
├── 3-disadvantages.txt
├── 4-comparison_with_sql.txt
└── README.md   ← this file
```

