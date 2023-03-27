# 📁 Files 

## FileListAPI
Endpoint to fetch all files

### GET: `/api/files`

### Headers
| Content-Type  | Value     |
|---------------|-----------|
| Authorization | jwt_token |


### Response
```json
{
    "status": 200,
    "message": "string",
    "file": [
        {
            "file_id": "uuid",
            "html_file": "file_url",
            "pdf_file": "file_url",
            "uploaded_at": "datetime",
            "converted_at": "datetime",
            "created_at": "datetime",
            "updated_at": "datetime"
        }
    ]
}
```

---

## FileListAPI
Endpoint to delete all files

### DELETE: `/api/files`

### Headers
| Content-Type  | Value     |
|---------------|-----------|
| Authorization | jwt_token |


### Response
```json
{
    "status": 200,
    "message": "string"
}
```

---

## FileDetailAPI
Endpoint to get a file details

### GET: `/api/files/<file_id>`

### Headers
| Content-Type  | Value     |
|---------------|-----------|
| Authorization | jwt_token |

### Response
```json
{
  "status": 200,
  "message": "string",
  "file": {
      "file_id": "uuid",
      "html_file": "file_url",
      "pdf_file": "file_url",
      "uploaded_at": "datetime",
      "converted_at": "datetime",
      "created_at": "datetime",
      "updated_at": "datetime"
  }
}
```

---

## FileDetailAPI
Endpoint to delete a file

### DELETE: `/api/files/<file_id>`

### Headers
| Content-Type  | Value     |
|---------------|-----------|
| Authorization | jwt_token |


### Response
```json
{
    "status": 200,
    "message": "string"
}
```
