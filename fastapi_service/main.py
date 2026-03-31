from fastapi import FastAPI
import requests
import psycopg2

app = FastAPI()

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "db",
    "port": "5432"
}

@app.get("/api/health")
def health():
    return {"status": "FastAPI running"}

@app.post("/api/ingest")
def ingest_data():
    response = requests.get("http://flask:5000/api/customers")
    data = response.json()["data"]

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id VARCHAR(50) PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR(100),
        phone VARCHAR(20),
        address TEXT,
        date_of_birth DATE,
        account_balance FLOAT,
        created_at DATE
    )
    """)

    for c in data:
        cur.execute("""
        INSERT INTO customers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (customer_id) DO NOTHING
        """, (
            c['customer_id'], c['first_name'], c['last_name'],
            c['email'], c['phone'], c['address'],
            c['date_of_birth'], c['account_balance'], c['created_at']
        ))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Data ingested successfully"}