from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

try:
    file_path = os.path.join(os.path.dirname(__file__), 'customers.json')
    with open(file_path) as f:
        customers = json.load(f)
    print(f"✅ Loaded {len(customers)} customers")
except Exception as e:
    print("❌ Error loading JSON:", e)
    customers = []

@app.route('/api/health')
def health():
    return {"status": "Flask running"}

@app.route('/api/customers', methods=['GET'])
def get_customers():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
    except:
        return {"error": "Invalid pagination params"}, 400

    start = (page - 1) * limit
    end = start + limit

    if not customers:
        return {
            "data": [],
            "message": "No data found",
            "total": 0,
            "page": page,
            "limit": limit
        }

    return jsonify({
        "data": customers[start:end],
        "total": len(customers),
        "page": page,
        "limit": limit
    })

@app.route('/api/customers/<id>', methods=['GET'])
def get_customer(id):
    for c in customers:
        if c.get('customer_id') == id:
            return jsonify(c)

    return {"error": "Customer not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)