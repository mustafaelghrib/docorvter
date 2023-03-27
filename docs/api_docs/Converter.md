# 📁 Converter 

## HtmlConverterAPI
Endpoint for converting an HTML file to PDF file

### POST: `/api/html/convert`

### Headers
| Content-Type  | Value     |
|---------------|-----------|
| Authorization | jwt_token |


### Body
| Param     | value     | Type |
|-----------|-----------|------|
| html_file | file.html | file |


### Response
```json
{
    "status": 200,
    "message": "string"
}
```
