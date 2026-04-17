# 🚀 Multitasking AI - Backend Assessment

## 📌 Overview

This project demonstrates a complete backend pipeline using:

* **Flask** → Mock customer data API
* **FastAPI** → Data ingestion pipeline
* **PostgreSQL** → Data storage
* **Docker Compose** → Multi-service orchestration

### 🔄 Data Flow

```
Flask (JSON API) → FastAPI (Ingestion) → PostgreSQL → API Response
```

---

## 🏗️ Project Structure

```
project-root/
├── docker-compose.yml
├── README.md
├── mock-server/
│   ├── app.py
│   ├── data/customers.json
│   ├── Dockerfile
│   └── requirements.txt
└── pipeline-service/
    ├── main.py
    ├── models/customer.py
    ├── services/ingestion.py
    ├── database.py
    ├── Dockerfile
    └── requirements.txt
```

---

## ⚙️ Tech Stack

* **Flask** – REST API for mock data
* **FastAPI** – High-performance API for ingestion
* **PostgreSQL** – Relational database
* **SQLAlchemy** – ORM
* **dlt** – Data ingestion library
* **Docker & Docker Compose** – Containerization

---

## 🧪 Features

### ✅ Flask Mock Server

* Serves customer data from JSON file
* Pagination support (`page`, `limit`)
* Fetch single customer
* Health check endpoint

### ✅ FastAPI Pipeline

* Fetches data from Flask API
* Handles automatic pagination
* Inserts/updates data in PostgreSQL (Upsert)
* Provides API to query stored data

---

## 📡 API Endpoints

### 🔹 Flask (Port: 5000)

| Endpoint              | Method | Description         |
| --------------------- | ------ | ------------------- |
| `/api/customers`      | GET    | Paginated customers |
| `/api/customers/{id}` | GET    | Get customer by ID  |
| `/api/health`         | GET    | Health check        |

#### Example Response

```json
{
  "data": [],
  "total": 20,
  "page": 1,
  "limit": 10
}
```

---

### 🔹 FastAPI (Port: 8000)

| Endpoint              | Method | Description             |
| --------------------- | ------ | ----------------------- |
| `/api/ingest`         | POST   | Fetch & store data      |
| `/api/customers`      | GET    | Get paginated customers |
| `/api/customers/{id}` | GET    | Get customer by ID      |

#### Example Ingest Response

```json
{
  "status": "success",
  "records_processed": 20
}
```

---

## 🐳 Docker Setup

### 🔧 docker-compose.yml Services

* **postgres** → Database (Port: 5432)
* **mock-server** → Flask API (Port: 5000)
* **pipeline-service** → FastAPI (Port: 8000)

---

## ▶️ Getting Started

### 1️⃣ Clone Repository

```
git clone https://github.com/newton701/multitasking_AI.git
cd multitasking_AI
```

---

### 2️⃣ Start Services

```
docker-compose up -d
```

---

### 3️⃣ Verify Running Containers

```
docker ps
```

---

## 🧪 Testing APIs

### 🔹 Test Flask API

```
curl http://localhost:5000/api/customers?page=1&limit=5
```

---

### 🔹 Ingest Data into PostgreSQL

```
curl -X POST http://localhost:8000/api/ingest
```

---

### 🔹 Fetch Stored Data

```
curl http://localhost:8000/api/customers?page=1&limit=5
```

---

## 🗄️ Database Schema

**Table: customers**

| Column          | Type             |
| --------------- | ---------------- |
| customer_id     | VARCHAR(50) (PK) |
| first_name      | VARCHAR(100)     |
| last_name       | VARCHAR(100)     |
| email           | VARCHAR(255)     |
| phone           | VARCHAR(20)      |
| address         | TEXT             |
| date_of_birth   | DATE             |
| account_balance | DECIMAL(15,2)    |
| created_at      | TIMESTAMP        |

---

## ⚠️ Error Handling

* 404 for missing customers
* Graceful API failures
* Database connection handling
* Pagination validation

---

## 📊 Evaluation Checklist

* [x] Flask serves paginated data
* [x] FastAPI ingests data correctly
* [x] PostgreSQL stores data
* [x] Docker Compose runs all services
* [x] API endpoints working

---

## 💡 Notes

* Ensure Docker is installed and running
* Ports 5000, 8000, and 5432 must be free
* Use `.env` for production secrets (recommended)

---

## 👨‍💻 Author

**Newton Dakua**

---

## ⭐ Conclusion

This project demonstrates a real-world microservice pipeline with:

* API communication
* Data ingestion
* Database persistence
* Containerized deployment

---
