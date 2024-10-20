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

# Define a User model
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




# Function to push the backup to GitHub
def push_to_github():
    try:
        # Set global git config for user.name and user.email
        subprocess.run(["git", "config", "user.email", "RenderAutomatedcommit@example.com"], check=True)
        subprocess.run(["git", "config", "user.name", "RenderAutomatedcommit"], check=True)
        
        # Add, commit, and push the backup file
        subprocess.run(["git", "add", "backup.sql"], check=True)
        subprocess.run(["git", "commit", "-m", "Automated backup of the database"], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during git push: {e}")






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
        return jsonify({'message': 'Username already exists'}), 400

    # Create a new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    # Export the database and push to GitHub
    export_database()
    push_to_github()

    return jsonify({'message': 'Registration successful'}), 201

# Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check credentials
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Show all users (without passwords)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.with_entities(User.username).all()
    user_list = [username for (username,) in users]  # Unpack the tuple
    return jsonify({'users': user_list}), 200

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
