# Database Design Document

## Introduction
This is the database design of `Docorvter`, and it is designed to store data related to users and files.
The database will be used by a document converter to manage and convert files.

---

## Entity-Relationship Diagram (ERD)
The ERD for `Docorvter` database is shown below:

[INSERT IMAGE OF ERD]

---

## Tables

### User
| Column     | Type        | Constraints |
|------------|-------------|-------------|
| user_id    | UUID        | PRIMARY KEY |
| email      | String(255) | NOT NULL    |
| username   | String(50)  | NOT NULL    |
| password   | String(255) | NOT NULL    |
| token      | String(255) | NULL        |
| created_at | Datetime    | NOT NULL    |
| updated_at | Datetime    | NULL        |

### File
| Column                                         | Type          | Constraints |
|------------------------------------------------|---------------|-------------|
| file_id                                        | UUID          | PRIMARY KEY |
| html_file                                      | File          | NULL        |
| pdf_file                                       | File          | NULL        |
| uploaded_at                                    | Datetime(255) | NULL        |
| converted_at                                   | Datetime(255) | NULL        |
| created_at                                     | Datetime      | NOT NULL    |
| updated_at                                     | Datetime      | NULL        |
| FOREIGN KEY (user_id) REFERENCES User(user_id) |

---

## Columns

### User
- **user_id**: Unique identifier for each user.
- **email**: The user's email address for communication and notifications.
- **username**: The user's username for logging into the system.
- **password**: The user's password, stored as a salted hash.
- **token**: The user's token, used when access other endpoints.
- **created_at**: The datetime when the user is created
- **updated_at**: The updated datetime when updating the user

### File
- **file_id**: Unique identifier for each file.
- **html_file**: The html file that uploaded for conversion.
- **pdf_file**: The pdf file path that converted.
- **converted_at**: The datetime when uploading the file.
- **converted_at**: The datetime when converting the file.
- **created_at**: The datetime when the file is created.
- **updated_at**: The updated datatime when updating the file.

## Relationships
* Users and Files: A user can convert many files, but each file belongs to only one user.

---

## Conclusion
The `Docorvter` database is designed to support the needs of the document converter 
by providing a centralized location for managing users and files.
