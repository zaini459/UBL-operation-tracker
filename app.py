import os
import random
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database array with sample seed records
accounts_db = [
    { "id": "UBL-9011", "name": "Zainab Sarfraz", "type": "UBL Business Partner", "bio": True, "cnic": True, "source": True, "status": "Approved" },
    { "id": "UBL-9012", "name": "Ahmed Shah", "type": "Asaan Account", "bio": True, "cnic": True, "source": False, "status": "Pending" },
    { "id": "UBL-9013", "name": "Fatima Khan", "type": "Current Regular", "bio": False, "cnic": True, "source": False, "status": "Compliance Hold" }
]

@app.route('/')
def home():
    # Render static frontend dashboard
    return render_template('index.html')

@app.route('/api/records', methods=['GET'])
def get_records():
    # Return master logs to interface
    return jsonify(accounts_db), 200

@app.route('/api/register-log', methods=['POST'])
def register_log():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid form submission payload"}), 400
    
    name = data['name']
    acc_type = data['type']
    bio = data['bio']
    cnic = data['cnic']
    source = data['source']
    
    # Core structural validation calculations matching business specifications
    if not bio or not cnic:
        computed_status = "Compliance Hold"
    elif not source:
        computed_status = "Pending"
    else:
        computed_status = "Approved"
        
    # Construct distinct primary tracking object entity
    new_record = {
        "id": f"UBL-{random.randint(1000, 9999)}",
        "name": name,
        "type": acc_type,
        "bio": bio,
        "cnic": cnic,
        "source": source,
        "status": computed_status
    }
    
    # Prepend operational transaction history logs
    accounts_db.insert(0, new_record)
    return jsonify({"success": True, "record": new_record}), 201

@app.route('/api/update-status', methods=['POST'])
def update_status():
    data = request.get_json()
    ref_id = data.get('id')
    new_status = data.get('status')
    
    # Search entity mapping inside reference structure logs
    for record in accounts_db:
        if record['id'] == ref_id:
            record['status'] = new_status
            return jsonify({"success": True, "message": "Compliance state mutated successfully"}), 200
            
    return jsonify({"error": "Record reference identifier not found"}), 404

if __name__ == '__main__':
    # Runs backend listener channel on distinct network port
    app.run(debug=True, port=5003)