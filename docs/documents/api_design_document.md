# API Design Document

## Overview
This API is designed for a document converter that enables users to convert files. 
The API provides endpoints for user authentication, files management, and file conversion.

---

## API Endpoints

The API endpoints and their HTTP methods are:

### Users
* /users/register: POST - register new user
* /users/login: POST - return JWT token

### Files
* /files: GET - returns a list of files
* /files: DELETE - delete all files
* /files/file_id: GET - get a file details
* /files/file_id: DELETE - delete a file

### Converter
* /html/convert: POST - convert HTML file to PDF file

---

## Request and Response
Refer the [API Documentation](../../api_docs) for more information.

## Authentication
The API uses token-based authentication with JSON Web Tokens (JWTs). 
To access the protected endpoints, clients must send a valid JWT in the Authorization header of the request. 
The server verifies the JWT and grants access to the endpoint if it's valid.

---

## Error Handling
The API uses HTTP status codes and error messages to communicate errors to clients. 
The following error codes may be returned:

* 200 OK: The request was successful.
* 400 BAD REQUEST: The request was invalid or could not be understood by the server.
* 401 Unauthorized: The client is not authorized to access the requested resource.
* 404 Not Found: The requested resource could not be found on the server.

---

## API Documentation
The API documentation is available at [/api-docs](../../api_docs) and follows the OpenAPI 3.0.0 specification. 
The documentation includes information about each endpoint, its parameters, responses, and examples.

---

## Conclusion
This API design document outlines the endpoints, request and response, 
authentication and authorization, error handling, and API documentation for the document converter. 
It follows a standardized format and provides a clear and concise overview of the APIs functionality.
