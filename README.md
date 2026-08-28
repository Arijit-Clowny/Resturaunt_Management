# 🍽️ Restaurant Management System

A Python-based **Restaurant Management System** designed to manage a multi-cuisine restaurant's menu, customer orders, cart, billing, checkout, and persistent order storage.

The project started as a console-based Python application and has since been extended with **MySQL database integration** and a **Tkinter-based graphical interface**. It uses **Object-Oriented Programming (OOP)** for order management, with a separate database layer for retrieving menu items and storing completed orders.

The project is structured so it can be further extended with **data analytics** and additional reporting features in the future.

---

## 📌 Project Overview

The Restaurant Management System allows a customer to:

- Browse different food categories through a graphical interface.
- Select vegetarian and non-vegetarian items.
- Add food items to an order.
- Specify quantities.
- Automatically combine repeated orders of the same food item.
- View the current cart/order summary.
- Remove items or reduce their quantity.
- Calculate the subtotal.
- Calculate GST.
- Generate the final bill.
- Confirm or cancel checkout.
- Store completed orders in MySQL.
- Store individual order items in MySQL.
- Retrieve menu items directly from MySQL.

---

# ✨ Current Features

## 1. Menu Management

The restaurant contains the following categories:

- Starters
  - Vegetarian
  - Non-Vegetarian
- Main Course
  - Vegetarian
  - Non-Vegetarian
- Bread / Rice
- Desserts
- Drinks

Menu information is stored in MySQL instead of being hard-coded inside the Python menu functions.

Each food item contains:

- Food ID
- Name
- Price
- Category
- Food Type

These values are represented in Python using the `FoodItem` class.

---

## 2. Object-Oriented Programming

The project uses Python OOP concepts to model the restaurant system.

### `FoodItem`

Represents an individual food item.

```python
class FoodItem:
    def __init__(self, index, name, price, category, food_type):
        self.index = index
        self.name = name
        self.price = price
        self.category = category
        self.food_type = food_type
```

---

## 3. Graphical User Interface (Tkinter)

The system now includes a full **Tkinter GUI** (`app.py`) built on top of the core order/cart/database logic:

- A styled header and background image.
- A category selection screen (Starters, Main Course, Bread/Rice, Desserts, Drinks).
- A dynamic menu panel that updates based on the selected category, split into Vegetarian and Non-Vegetarian sections where applicable.
- Quantity controls for adding items to the cart.
- A **View Cart** screen for reviewing, adjusting, and checking out an order.
- Hover effects on category buttons for a more responsive feel.

### GUI Project Structure

| File | Responsibility |
|---|---|
| `main.py` | Main Tkinter application: window setup, header, category navigation, menu rendering |
| `menu.py` | Retrieves food items (as `FoodItem` objects) from MySQL, filtered by category/type |
| `cart.py` | Cart UI components (quantity controls) and the cart/checkout screen |
| `order_service.py` | Places orders — writes the order and its line items to MySQL |
| `config.py` | Shared style constants (colors, fonts) and configuration values |
| `assets/` | Static assets used by the GUI (e.g. `resturant.jpeg` background image) |

---

## 4. Database Integration (MySQL)

- Menu items are read from MySQL at runtime via `menu.py`, rather than being hard-coded.
- Completed orders are persisted to MySQL via `order_service.py`, including:
  - The overall order record (subtotal, GST, total, timestamp).
  - Individual order line items (food item, quantity, price).
- This separation keeps the menu and order history editable and queryable outside the application itself.

---

## 🛠️ Requirements

- Python 3.x
- `mysql-connector-python` (or your preferred MySQL driver)
- `Pillow` (for image handling in the Tkinter GUI)
- A running MySQL server with the appropriate schema for menu items and orders

Install dependencies:

```bash
pip install mysql-connector-python Pillow
```

---

## ▶️ Running the Application

```bash
python main.py
```

This launches the Tkinter GUI, from which categories can be browsed, items added to the cart, and orders placed and stored in MySQL.

---

## 🚀 Future Scope

- Data analytics and reporting on order history (e.g. best-selling items, revenue trends).
- Admin-side menu management (add/edit/remove items directly from the GUI).
- Order history lookup and receipt printing/export.
- User accounts and saved order preferences.

---

## 📄 License

Add your preferred license here (e.g. MIT).
