# 🍽️ Restaurant Management System

A Python-based **Restaurant Management System** designed to manage a multi-cuisine restaurant's menu, customer orders, cart, billing, checkout, and persistent order storage.

The project started as a console-based Python application and has now been extended with **MySQL database integration**. It uses **Object-Oriented Programming (OOP)** for order management and a separate database layer for retrieving menu items and storing completed orders.

The project is structured so it can be further extended with a **Tkinter GUI** and **data analytics** in the future.

---

## 📌 Project Overview

The Restaurant Management System allows a customer to:

- Browse different food categories.
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

Menu information is now stored in MySQL instead of being hard-coded inside the Python menu functions.

Each food item contains:

```text
Food ID
Name
Price
Category
Food Type
