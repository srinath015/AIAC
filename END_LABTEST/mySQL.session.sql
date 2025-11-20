-- File: mySQL.session.sql
-- GitHub Copilot
-- Database schema and test queries for a book shop: authors, books, sales
-- Includes: table creation, sample data, queries for best-selling books,
-- an example "add author" statement, and a safe "update stock" transaction.
-- MySQL-compatible syntax

/* ==========================
    1) Schema: Authors, Books, Sales
    ========================== */

-- Drop tables if they exist
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Authors table
CREATE TABLE authors (
     author_id    INTEGER PRIMARY KEY AUTO_INCREMENT,
     full_name    VARCHAR(255) NOT NULL,
     birth_date   DATE,
     country      VARCHAR(100),
     biography    TEXT,
     created_at   DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Books table
CREATE TABLE books (
     book_id      INTEGER PRIMARY KEY AUTO_INCREMENT,
     title        VARCHAR(500) NOT NULL,
     author_id    INTEGER NOT NULL,
     isbn         VARCHAR(20) UNIQUE,
     price        DECIMAL(10,2) NOT NULL DEFAULT 0.00,
     stock        INTEGER NOT NULL DEFAULT 0,
     published_on DATE,
     created_at   DATETIME DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE RESTRICT
);

-- Sales table (each row = one sale transaction line)
CREATE TABLE sales (
     sale_id      INTEGER PRIMARY KEY AUTO_INCREMENT,
     book_id      INTEGER NOT NULL,
     sale_date    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     quantity     INTEGER NOT NULL CHECK (quantity > 0),
     unit_price   DECIMAL(10,2) NOT NULL,
     total_price  DECIMAL(12,2) NOT NULL,
     customer_note TEXT,
     FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE RESTRICT
);

-- Indexes for typical queries
CREATE INDEX idx_sales_book ON sales(book_id);
CREATE INDEX idx_books_author ON books(author_id);
CREATE INDEX idx_sales_date ON sales(sale_date);


-- ==========================
-- 2) Sample/test data
-- ==========================

-- Insert sample authors
INSERT INTO authors (full_name, birth_date, country, biography)
VALUES
  ('Jane A. Reader', '1975-03-12', 'USA', 'Fiction author, writes thrillers.'),
  ('Samuel B. Page', '1968-11-02', 'UK', 'Non-fiction writer on computing.');

-- Insert sample books
INSERT INTO books (title, author_id, isbn, price, stock, published_on)
VALUES
  ('The Last Chapter', 1, '978-0-111111-11-1', 19.99, 50, '2020-06-15'),
  ('Learning SQL Fast', 2, '978-0-222222-22-2', 29.50, 30, '2019-09-01'),
  ('Advanced Databases', 2, '978-0-333333-33-3', 45.00, 20, '2021-02-20');

-- Insert sample sales (simulate multiple purchases)
INSERT INTO sales (book_id, sale_date, quantity, unit_price, total_price)
VALUES
  (1, '2024-01-05', 3, 19.99, 59.97),
  (2, '2024-01-07', 5, 29.50, 147.50),
  (2, '2024-01-10', 2, 29.50, 59.00),
  (3, '2024-01-12', 1, 45.00, 45.00),
  (1, '2024-01-15', 7, 19.99, 139.93),
  (2, '2024-02-01', 4, 29.50, 118.00);


-- ==========================
-- 3) Query: List best-selling books
--    - By total quantity sold (descending)
--    - Shows book, author, total_sold, revenue
-- ==========================

-- Full ranked list (all books)
SELECT
  b.book_id,
  b.title,
  a.full_name AS author,
  COALESCE(SUM(s.quantity), 0)    AS total_sold,
  COALESCE(SUM(s.total_price), 0) AS revenue
FROM books b
LEFT JOIN authors a ON b.author_id = a.author_id
LEFT JOIN sales s    ON b.book_id = s.book_id
GROUP BY b.book_id, b.title, a.full_name
ORDER BY total_sold DESC, revenue DESC;

-- Top N best-sellers example: top 10
SELECT
  b.book_id,
  b.title,
  a.full_name AS author,
  COALESCE(SUM(s.quantity), 0)    AS total_sold,
  COALESCE(SUM(s.total_price), 0) AS revenue
FROM books b
LEFT JOIN authors a ON b.author_id = a.author_id
LEFT JOIN sales s    ON b.book_id = s.book_id
GROUP BY b.book_id, b.title, a.full_name
ORDER BY total_sold DESC, revenue DESC
LIMIT 10;


-- ==========================
-- 4) Statement: Add a new author
--    - Template and example
-- ==========================

-- Template (use parameters in your application):
-- INSERT INTO authors (full_name, birth_date, country, biography) VALUES (?, ?, ?, ?);

-- Example raw insert:
INSERT INTO authors (full_name, birth_date, country, biography)
VALUES ('A. New Author', '1980-05-20', 'Canada', 'Newcomer to our store catalogue.');

-- After inserting, get the new author id:
-- SELECT LAST_INSERT_ID();


-- ==========================
-- 5) Statement: Update stock safely (reduce stock when sale occurs)
--    - Example transaction that checks availability and records sale.
-- ==========================

-- Example parameters (replace with application variables)
-- @book_id = id of book to sell
-- @qty = quantity to deduct (integer)
-- @unit_price = price captured for sale

-- Transactional example for MySQL:
START TRANSACTION;

-- Check stock and update atomically: only succeed if enough stock
UPDATE books
SET stock = stock - 3
WHERE book_id = 2
  AND stock >= 3;

-- If update affected 1 row, record the sale:
INSERT INTO sales (book_id, quantity, unit_price, total_price)
VALUES (2, 3, 29.50, 87.50);

COMMIT;

-- Simpler single-statement stock update (no transaction):
-- UPDATE books SET stock = stock - 3 WHERE book_id = 2 AND stock >= 3;


-- ==========================
-- 6) Quick test queries to validate state
-- ==========================

-- 1) See current books and stock
SELECT book_id, title, stock, price FROM books ORDER BY book_id;

-- 2) See sales history
SELECT sale_id, sale_date, book_id, quantity, unit_price, total_price FROM sales ORDER BY sale_date;

-- 3) Best-sellers (re-run)
SELECT
  b.book_id,
  b.title,
  a.full_name AS author,
  COALESCE(SUM(s.quantity), 0)    AS total_sold,
  COALESCE(SUM(s.total_price), 0) AS revenue
FROM books b
LEFT JOIN authors a ON b.author_id = a.author_id
LEFT JOIN sales s    ON b.book_id = s.book_id
GROUP BY b.book_id, b.title, a.full_name
ORDER BY total_sold DESC;

-- End of script
