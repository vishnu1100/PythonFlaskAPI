from flask import Flask, jsonify, request
from flask_cors import CORS
import hashlib
import csv
import os

app = Flask(__name__)
CORS(app, origins=["*"])  # Allow the specific origin

# File path for the "database"
CSV_FILE = 'users_db.csv'

# Utility function to hash passwords using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Utility function to read the CSV and return users as a dictionary
def read_users_from_csv():
    users = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    username, hashed_password = row
                    users[username] = hashed_password
    return users

# Utility function to write a new user to the CSV
def write_user_to_csv(username, hashed_password):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your API!"})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data. Username and password are required."}), 400

    username = data['username']
    password = data['password']

    users_db = read_users_from_csv()  # Load users from CSV

    if username in users_db:
        return jsonify({"error": "User already exists."}), 400

    hashed_password = hash_password(password)
    write_user_to_csv(username, hashed_password)  # Write the new user to CSV
    return jsonify({"message": f"User {username} registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data. Username and password are required."}), 400

    username = data['username']
    password = data['password']

    users_db = read_users_from_csv()  # Load users from CSV
    hashed_password = hash_password(password)

    if username in users_db and users_db[username] == hashed_password:
        return jsonify({"message": f"Welcome {username}! You are successfully logged in."})
    else:
        return jsonify({"error": "Invalid username or password."}), 401

if __name__ == '__main__':
    # Create the CSV file if it doesn't exist
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password'])  # Write header (optional)
    app.run(debug=True)
