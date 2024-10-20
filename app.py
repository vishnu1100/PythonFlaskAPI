from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS  #### Import CORS

app = Flask(__name__)

CORS(app, origins=["*"])  #### Allow the specific origin 

# CSV file to store user data
CSV_FILE = 'users.csv'

# Initialize the CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['username', 'password'])
    df.to_csv(CSV_FILE, index=False)

# Helper function to save data to CSV
def save_to_csv(username, password):
    df = pd.read_csv(CSV_FILE)
    df = df.append({'username': username, 'password': password}, ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

# Helper function to check login credentials
def check_credentials(username, password):
    df = pd.read_csv(CSV_FILE)
    user = df[(df['username'] == username) & (df['password'] == password)]
    return not user.empty

# Registration Route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    df = pd.read_csv(CSV_FILE)
    if username in df['username'].values:
        return jsonify({'message': 'Username already exists'}), 400

    # Save new user to CSV
    save_to_csv(username, password)
    return jsonify({'message': 'Registration successful'}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check credentials
    if check_credentials(username, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Show all users (without passwords)
@app.route('/users', methods=['GET'])
def get_users():
    df = pd.read_csv(CSV_FILE)
    users = df['username'].tolist()  # Only return usernames, not passwords
    return jsonify({'users': users}), 200

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
