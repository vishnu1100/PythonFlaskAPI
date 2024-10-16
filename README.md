
# Flask Free API 

This API allows users to get all available API for free.

## Base URL

```
https://pythonflaskapi-4pjy.onrender.com/
```

---

## Endpoints

### 1. Home

- **URL**: `/`
- **Method**: `GET`

**Example Response**:

```json
{
  "message": "Welcome to your API!"
}
```

---

### 2. Register User



- **URL**: `/register`
- **Method**: `POST`


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




---

### 3. Login User


- **URL**: `/login`
- **Method**: `POST`


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



---
<!-- 
### 4. cities

- **URL**: `/cities`
- **Method**: `GET`

**Example Response**:

```json
{
  "message": "Welcome to your API!"
}
```

--- -->
