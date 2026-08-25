-- =========================================================
-- RESTAURANT MANAGEMENT SYSTEM
-- Database Setup Script
-- =========================================================

-- Create database
CREATE DATABASE IF NOT EXISTS restaurant_db;

-- Select database
USE restaurant_db;


-- =========================================================
-- FOOD ITEMS TABLE
-- Stores all items available on the restaurant menu
-- =========================================================

CREATE TABLE IF NOT EXISTS food_items (
    food_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    food_type VARCHAR(20)
);


-- =========================================================
-- ORDERS TABLE
-- Stores information about each completed order
-- =========================================================

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    subtotal DECIMAL(10,2) NOT NULL,
    gst DECIMAL(10,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL
);


-- =========================================================
-- ORDER ITEMS TABLE
-- Stores individual items belonging to an order
-- =========================================================

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    food_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (food_id)
        REFERENCES food_items(food_id)
);


-- =========================================================
-- MENU DATA
-- =========================================================

INSERT INTO food_items
(food_id, name, price, category, food_type)
VALUES

-- -------------------------
-- VEG STARTERS
-- -------------------------

(1, 'Paneer Tikka', 250.00, 'Starter', 'Veg'),
(2, 'Crispy Chilli Baby Corn', 200.00, 'Starter', 'Veg'),
(3, 'Hara Bhara Kebab', 160.00, 'Starter', 'Veg'),
(4, 'Veg Manchurian', 180.00, 'Starter', 'Veg'),
(5, 'Chilli Mushroom', 220.00, 'Starter', 'Veg'),

-- -------------------------
-- NON-VEG STARTERS
-- -------------------------

(6, 'Chicken Tikka', 300.00, 'Starter', 'Non-Veg'),
(7, 'Chilli Chicken', 260.00, 'Starter', 'Non-Veg'),
(8, 'Fish Fingers', 280.00, 'Starter', 'Non-Veg'),
(9, 'Chicken 65', 240.00, 'Starter', 'Non-Veg'),
(10, 'Mutton Seekh Kebab', 380.00, 'Starter', 'Non-Veg'),

-- -------------------------
-- VEG MAIN COURSE
-- -------------------------

(11, 'Soya Chunks Masala', 180.00, 'Main Course', 'Veg'),
(12, 'Palak Paneer', 280.00, 'Main Course', 'Veg'),
(13, 'Kadai Paneer', 290.00, 'Main Course', 'Veg'),
(14, 'Dal Tadka', 180.00, 'Main Course', 'Veg'),
(15, 'Vegetable Jalfrezi', 240.00, 'Main Course', 'Veg'),

-- -------------------------
-- NON-VEG MAIN COURSE
-- -------------------------

(16, 'Grilled Chicken Breast', 400.00, 'Main Course', 'Non-Veg'),
(17, 'Chicken Tikka Masala', 350.00, 'Main Course', 'Non-Veg'),
(18, 'Macher Jhol (Fish Curry)', 300.00, 'Main Course', 'Non-Veg'),
(19, 'Mutton Rogan Josh', 450.00, 'Main Course', 'Non-Veg'),
(20, 'Bhuna Gosht', 480.00, 'Main Course', 'Non-Veg'),

-- -------------------------
-- BREAD / RICE
-- -------------------------

(21, 'Butter Naan', 30.00, 'Bread/Rice', NULL),
(22, 'Naan', 20.00, 'Bread/Rice', NULL),
(23, 'Tawa Roti', 10.00, 'Bread/Rice', NULL),
(24, 'Jeera Rice', 100.00, 'Bread/Rice', NULL),
(25, 'Biryani', 160.00, 'Bread/Rice', NULL),
(26, 'Fried Rice (Veg)', 150.00, 'Bread/Rice', 'Veg'),

-- -------------------------
-- DESSERTS
-- -------------------------

(27, 'Ice Cream', 110.00, 'Dessert', NULL),
(28, 'Brownie', 120.00, 'Dessert', NULL),
(29, 'Gulab Jamun and Ice Cream', 160.00, 'Dessert', NULL),
(30, 'Blueberry Cheesecake', 140.00, 'Dessert', NULL),
(31, 'Rabdi Jalebi', 120.00, 'Dessert', NULL),

-- -------------------------
-- DRINKS
-- -------------------------

(32, 'Cold Drinks', 90.00, 'Drinks', NULL),
(33, 'Virgin Mojito', 120.00, 'Drinks', NULL),
(34, 'Blue Lagoon', 120.00, 'Drinks', NULL),
(35, 'Lemonade', 110.00, 'Drinks', NULL),
(36, 'Lassi', 90.00, 'Drinks', NULL);