-- Retail Store Inventory system


-- Clean up if re-running
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

-- Categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255)
);

-- Products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category_id INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    CONSTRAINT FK_Products_Categories FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Sales
CREATE TABLE Sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    sale_date DATETIME NOT NULL DEFAULT NOW(),
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL, -- price at time of sale
    CONSTRAINT FK_Sales_Products FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Insert sample categories
INSERT INTO Categories (name, description) VALUES
('Electronics', 'Phones, laptops, accessories'),
('Home Appliances', 'Kitchen and home appliances'),
('Clothing', 'Men and women apparel');

-- Insert sample products (category_id corresponds to insertion order above)
INSERT INTO Products (name, category_id, unit_price, stock) VALUES
('Smartphone X', 1, 699.99, 50),
('Laptop Pro', 1, 1299.00, 20),
('Wireless Headphones', 1, 149.99, 100),
('Blender 3000', 2, 89.50, 40),
('Air Fryer', 2, 149.00, 30),
('T-Shirt', 3, 19.99, 200),
('Jeans', 3, 49.99, 150);

-- Insert sample sales (product_id corresponds to insertion order above)
INSERT INTO Sales (product_id, sale_date, quantity, unit_price) VALUES
(1, '2025-11-01', 2, 699.99),
(2, '2025-11-02', 1, 1299.00),
(3, '2025-11-03', 5, 139.99), 
(4, '2025-11-04', 3, 89.50),
(5, '2025-11-05', 2, 149.00),
(6, '2025-11-05', 10, 19.99),
(7, '2025-11-06', 4, 49.99);

-- Calculate total sales per category
-- total_sales = SUM(quantity * unit_price)
SELECT
    c.category_id,
    c.name AS category_name,
    COALESCE(SUM(s.quantity * s.unit_price), 0) AS total_sales,
    COALESCE(SUM(s.quantity), 0) AS total_units_sold
FROM Categories c
LEFT JOIN Products p ON p.category_id = c.category_id
LEFT JOIN Sales s ON s.product_id = p.product_id
GROUP BY c.category_id, c.name
ORDER BY total_sales DESC;