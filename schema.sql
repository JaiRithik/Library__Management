-- NOTE: This schema seeds demo/sample data only, including a placeholder 
-- admin account ('Admin' / '1234') and a placeholder member account. 
-- Change or remove these before using this database anywhere but a local 
-- demo, since passwords are stored in plain text by this application. 
CREATE DATABASE IF NOT EXISTS library_management; 
USE library_management; 
CREATE TABLE administration ( 
    admin_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(255) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL, 
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP 
); 
INSERT INTO administration (username, password) 
VALUES ('Admin', '1234'); 
CREATE TABLE books ( 
    book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    title VARCHAR(100) NOT NULL, 
    author VARCHAR(50) NOT NULL, 
    genre VARCHAR(50), 
    quantity INT DEFAULT 0, 
    rating DECIMAL(3,2), 
    purchase_date DATE , 
    invoice_no VARCHAR(20) NOT NULL DEFAULT 'UNKNOWN', 
 
    publisher_name VARCHAR(100) NOT NULL DEFAULT 'UNKNOWN', 
    store_name VARCHAR(100) NOT NULL DEFAULT 'UNKNOWN', 
    amt DECIMAL(10,2) NOT NULL DEFAULT 0.00 
); 
INSERT INTO books (title, author, genre, quantity, rating, purchase_date) 
VALUES  
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1, 4, '2025-05-10'), 
('1984', 'George Orwell', 'Dystopian', 4, 5, '2025-05-10'), 
('Pride and Prejudice', 'Jane Austen', 'Romance', 3, 3, '2025-05-10'), 
('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', -7, 4, '2025-05-10'), 
('Moby Dick', 'Herman Melville', 'Adventure', 1, 2, '2025-05-10'), 
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 5, 5, '2025-05-10'), 
('War and Peace', 'Leo Tolstoy', 'Historical Fiction', 2, 3, '2025-05-10'), 
('Jane Eyre', 'Charlotte Brontë', 'Romance', 2, 4, '2025-05-10'), 
('The Catcher in the Rye', 'J.D. Salinger', 'Coming-of-Age', 3, 2, '2025-05-10'), 
('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 3, 5, '2025-05-10'); 
CREATE TABLE members ( 
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(50) NOT NULL UNIQUE, 
    password VARCHAR(255) NOT NULL, 
    full_name VARCHAR(100), 
    email VARCHAR(100), 
    phone VARCHAR(20), 
    address VARCHAR(255), 
    joined_date DATE 
); 
INSERT INTO members (username, password, full_name, email, phone, address, 
joined_date) 
VALUES 
('User', 
'1234', 
'UserInterface', 
'userinterface@gmail.com', 
'9870645321', '7, Park Avenue.', '2025-05-02'); 
CREATE TABLE transactions ( 
    transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    book_id INT, 
    member_id INT, 
    borrow_date DATE, 
    return_date DATE, 
    expected_date DATE, 
    rating INT, 
    fees DECIMAL(10,2) DEFAULT 0.00, 
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE, 
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE 
); 
INSERT INTO transactions (book_id, member_id, borrow_date, return_date, 
expected_date, rating, fees) 
 
VALUES 
(1, 1, '2025-05-01', '2025-05-10', '2025-05-08', 4, 0.00), 
(2, 1, '2025-05-01', NULL, '2025-06-30', NULL, 0.00), 
(3, 1, '2025-05-02', '2025-05-25', '2025-06-30', 3, 0.00), 
(4, 1, '2025-05-03', NULL, '2025-07-01', NULL, 0.00), 
(5, 1, '2025-05-04', '2025-05-20', '2025-07-03', 2, 0.00), 
(6, 1, '2025-05-05', NULL, '2025-07-04', NULL, 0.00), 
(7, 1, '2025-05-06', NULL, '2025-07-05', NULL, 0.00), 
(8, 1, '2025-05-07', '2025-06-07', '2025-07-06', 4, 0.00), 
(9, 1, '2025-05-08', NULL, '2025-07-07', NULL, 0.00), 
(10,1, '2025-05-09', '2025-06-15', '2025-07-08', 5, 0.00);
