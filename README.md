
# Flask Login Reg API


# User Management API Documentation Using Flask
 This API supports user registration, login, and displaying all registered users.
## Installation
 To install and run the application,
  follow these steps:
1. Clone the repository:
    `git clone <repository-url>`
2. Navigate to the project directory: `cd <project-directory>`
3. Install dependencies: `pip install -r requirements.txt` 
4. Run the application: `python app.py` 
## Base URL [https://pythonflaskapi-gvv5.onrender.com/](https://pythonflaskapi-gvv5.onrender.com/) 
## API Endpoints 
### 1. Registration **Endpoint:** `/register`  
**Method:** POST  
**Request Parameters:** - `username` (string): 
The username of the new user. - `password` (string): 
The password for the new user. 
**Response:** 
```json { "message": "Registration successful" } ``` 
### 2. Login 
**Endpoint:** `/login`  
**Method:** POST  
**Request Parameters:** - `username` (string): The username of the user. - `password` (string): The password of the user. 
**Response:** ```json { "message": "Login successful" } ``` 
### 3. Get Users 
**Endpoint:** `/users`  
**Method:** GET  
**Response:** ```json { "users": ["user1", "user2", "user3"] } ``` 
## Usage Examples Below are examples of how to use the API with Postman or cURL: 
### Registration Example (cURL) ```bash curl -X POST https://pythonflaskapi-gvv5.onrender.com/register -d "username=your_username&password=your_password" ``` 
### Login Example (cURL) ```bash curl -X POST https://pythonflaskapi-gvv5.onrender.com/login -d "username=your_username&password=your_password" ``` 
## Contribution You can contribute to this project on [GitHub](https://github.com/vishnu1100/PythonFlaskAPI). 
## Contact Me [Here](https://vishnusanthosh.info/)

# Disclaimer 
## This API is for testing frontend apps functionality in login and registration through API request, so after every 24hr the complete database will be flushed.
