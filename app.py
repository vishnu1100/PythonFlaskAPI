from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sqlite3
import subprocess

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, origins=["*"])  # Allow CORS for all origins

# Define a User models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Function to export database to SQL file
def export_database():
    conn = sqlite3.connect('users.db')
    with open('backup.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()









# Default route for root URL
@app.route('/')
def home():
    return render_template('home.html')  # Render the HTML template

# Registration Route
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists code 400'}), 400

    # Create a new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    # Export the database and push to GitHub
    export_database()
    

    return jsonify({'message': 'Registration successful code 201'}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check credentials
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return jsonify({'message': 'Login successful code 200'}), 200
    else:
        return jsonify({'message': 'Invalid credentials code 401'}), 401

# Show all users (without passwords)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.with_entities(User.username).all()
    user_list = [username for (username,) in users]  # Unpack the tuple
    return jsonify({'users': user_list}), 200

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
