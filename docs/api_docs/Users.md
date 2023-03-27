# 📁 Users 

## UserRegisterAPI
Endpoint for user register

### POST: `/api/users/register`

### Body
```json
{
    "email": "string",
    "username": "string",
    "password": "string"
}
```

### Response (Success)
```json
{
    "status": 200,
    "message": "string",
    "user": {
        "user_id": "uuid",
        "email": "string",
        "username": "string",
        "created_at": "datetime",
        "updated_at": "datetime"
    }
}
```

### Response (Error)
```json
{
    "status": 400,
    "message": "string",
    "email_error": "string",
    "username_error": "string",
    "password_error": "string"
}
```

---

## UserLoginAPI
Endpoint for user login

### POST: `/api/users/login`

### Body
```json
{
    "email": "string",
    "password": "string"
}
```

### Response (Success)
```json
{
    "status": 200,
    "message": "string",
    "token": "jwt_token"
}
```

### Response (Error)
```json
{
    "status": 400,
    "message": "string",
    "email_error": "string",
    "password_error": "string"
}
```
