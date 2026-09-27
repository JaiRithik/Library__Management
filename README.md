# Library Management System

A Python-based Library Management System with a MySQL database backend. The project provides separate functionality for library administrators and members, including book management, borrowing and returning books, searching, ratings, due dates, and late-fee management.

## Features

### Administrator

* Administrator login
* Add new books
* Remove books
* Manage library records
* View and manage library information

### Member

* Member registration and login
* Search for books
* Search by title, author, genre, and rating
* Borrow books
* Return books
* Track due dates
* Handle late fees
* Rate books

## Technologies Used

* **Python**
* **MySQL**
* **SQL**

## Project Structure

```text
Library__Management/
│
├── main.py
├── users.py
├── book.py
├── library_administration.py
├── utilies.py
├── db_config.py
├── schema.sql
├── README.md
├── requirements.txt
└── .gitignore
```

## Database

The project uses MySQL to store library information.

The database schema is provided in:

```text
schema.sql
```

The database contains information required for users, administration, books, borrowing/returning, and related library operations.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/JaiRithik/Library__Management.git
cd Library__Management
```

### 2. Create the MySQL database

Open MySQL and execute the SQL commands in:

```text
schema.sql
```

### 3. Configure the database connection

Update the database configuration with your own local MySQL settings.

Do not commit passwords or other sensitive credentials to GitHub.

### 4. Install dependencies

If the project has external Python packages, install them using:

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

## Main Functionalities

The system supports:

* User registration and authentication
* Administrator authentication
* Book management
* Book searching
* Book borrowing
* Book returning
* Due-date tracking
* Late-fee handling
* Book ratings
* MySQL database storage

## Project Purpose

This project was developed as a practical implementation of programming, database management, and software development concepts using Python and MySQL.

## Author

**Jai Rithik**

GitHub:
https://github.com/JaiRithik

## Note

This project is intended for educational purposes. Database credentials and other private configuration values should be stored locally or through environment variables rather than committed to the repository.
