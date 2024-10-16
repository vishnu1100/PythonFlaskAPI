
# Flask User Registration and Login API

This API allows users to register and log in. User credentials are stored in a CSV file (`users_db.csv`). Passwords are hashed using SHA-256 for security.

## Base URL

```
https://pythonflaskapi-4pjy.onrender.com/
```

---

## Endpoints

### 1. Home

**Description**: A simple test endpoint to verify that the API is running.

- **URL**: `/`
- **Method**: `GET`
- **Response**: A welcome message.

**Example Response**:

```json
{
  "message": "Welcome to your API!"
}
```

---

### 2. Register User

**Description**: Registers a new user by accepting a username and password. The password is hashed and saved in the CSV file.

- **URL**: `/register`
- **Method**: `POST`
- **Request Body**:
  - JSON containing `username` and `password`.

**Example Request**:

```json
{
  "username": "testuser",
  "password": "mypassword123"
}
```

**Success Response**:

- **Code**: `200 OK`
- **Content**:

```json
{
  "message": "User testuser registered successfully!"
}
```

**Error Responses**:

- If the `username` or `password` is missing:

```json
{
  "error": "Invalid data. Username and password are required."
}
```

- If the `username` already exists:

```json
{
  "error": "User already exists."
}
```

---

### 3. Login User

**Description**: Logs in an existing user by validating their username and password.

- **URL**: `/login`
- **Method**: `POST`
- **Request Body**:
  - JSON containing `username` and `password`.

**Example Request**:

```json
{
  "username": "testuser",
  "password": "mypassword123"
}
```

**Success Response**:

- **Code**: `200 OK`
- **Content**:

```json
{
  "message": "Welcome testuser! You are successfully logged in."
}
```

**Error Responses**:

- If the `username` or `password` is missing:

```json
{
  "error": "Invalid data. Username and password are required."
}
```

- If the `username` does not exist or the password is incorrect:

```json
{
  "error": "Invalid username or password."
}
```

---

## File Storage

- User data (username and hashed password) is stored in a CSV file: `users_db.csv`.
- Each row in the CSV contains the following fields:
  - `username`: The user's username.
  - `password`: The hashed password (SHA-256).

---

## Error Handling

- If the request body is missing or improperly formatted, the API returns a `400 Bad Request` with a relevant error message.
- If a login attempt fails due to incorrect username or password, a `401 Unauthorized` response is returned.

---

## Example API Requests

### Register a New User

```bash
curl -X POST https://pythonflaskapi-4pjy.onrender.com/register \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "mypassword123"}'
```

### Log In a User

```bash
curl -X POST https://pythonflaskapi-4pjy.onrender.com/login \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "mypassword123"}'
```

---

## Notes

- **Security Considerations**: Passwords are hashed using SHA-256 before being stored. This is a basic security measure. In production systems, consider using more advanced techniques such as password salting and using a secure storage solution like a database.
- **CSV Storage**: This implementation uses a CSV file (`users_db.csv`) as a lightweight storage solution. For large-scale or production systems, it's better to use a relational database like MySQL or PostgreSQL, or a NoSQL database like MongoDB.
