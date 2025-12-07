# 📘 HTTP Requests & Working With Web Resources in Python

This project introduces how to interact with web resources using Python.
By the end of the project, you should be able to explain these concepts without using Google.

---

## 🎯 **Learning Objectives**

### General

* Understand how to fetch internet resources using the Python package **`urllib`**
* Decode the body of a response obtained via **`urllib`**
* Use the Python package **`requests`** (note: *requests is far simpler than urllib*)
* Perform **HTTP GET** requests
* Perform **HTTP POST/PUT/etc.** requests
* Fetch and process **JSON** resources
* Manipulate and use data from an external API or service

---

## 🧩 **1. Fetching Internet Resources with `urllib`**

`urllib` is a built-in Python library used to work with URLs and retrieve web data.

Example:

```python
from urllib import request

with request.urlopen("https://example.com") as response:
    data = response.read()
```

---

## 🔎 **2. Decoding `urllib` Response Body**

Responses from `urllib` come in **bytes**, so they must be decoded:

```python
decoded_data = data.decode("utf-8")
```

---

## 🚀 **3. Using the `requests` Package**

`requests` is a popular third-party library that makes HTTP requests much simpler than `urllib`.

Installation:

```bash
pip install requests
```

---

## 🌐 **4. Making an HTTP GET Request**

GET is used to retrieve data from a server.

```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)
print(response.text)
```

---

## ✍️ **5. Making HTTP POST/PUT/DELETE Requests**

### POST (send data):

```python
response = requests.post("https://api.example.com/users", data={"name": "Alice"})
```

### PUT (update data):

```python
response = requests.put("https://api.example.com/users/1", json={"age": 20})
```

### DELETE (remove data):

```python
response = requests.delete("https://api.example.com/users/1")
```

---

## 📦 **6. Fetching JSON Resources**

Most API responses are in JSON format.

```python
response = requests.get("https://api.example.com/user")
data = response.json()
print(data)
```

This automatically converts JSON into a Python dictionary.

---

## 🔧 **7. Manipulating Data From an External Service**

Once JSON is loaded, you can filter, sort, loop, or process it:

```python
users = response.json()

for user in users:
    print(user["name"])
```

Filtering example:

```python
students = [u for u in users if u["role"] == "student"]
```

---

## ✅ **Summary**

In this project, you learned how to:

* Retrieve web content using Python
* Use both `urllib` and `requests`
* Perform HTTP methods (GET, POST, PUT, DELETE)
* Work with JSON data
* Process and manipulate responses from external APIs

