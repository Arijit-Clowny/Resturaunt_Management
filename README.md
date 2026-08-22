# 🍽️ Restaurant Management System

A Python-based **Restaurant Management System** designed to manage a multi-cuisine restaurant's menu, customer orders, cart, billing, and checkout process.

The current version is a **console-based application** built using Python and Object-Oriented Programming (OOP) concepts. The project is intentionally structured so that it can be extended in the future with a **SQL database** for persistent data storage and a **Tkinter GUI** for a graphical user interface.

---

## 📌 Project Overview

The Restaurant Management System allows a customer to:

- Browse different food categories.
- Select vegetarian and non-vegetarian items.
- Add food items to an order.
- Specify quantities.
- Automatically combine repeated orders of the same food item.
- View the current cart/order summary.
- Calculate the total bill.
- Generate/display the bill.
- Confirm or cancel checkout.
- Clear the cart after a successful checkout.
- Exit the application.

The current application stores menu and order information in Python objects and memory. Once the program terminates, the order data is lost.

The planned future versions will introduce:

- **SQL/MySQL integration** for persistent storage.
- **Tkinter GUI** for a desktop graphical interface.
- A cleaner separation between the user interface, business logic, and database layer.

---

## ✨ Current Features

### 1. Menu Management

The restaurant currently contains the following categories:

- Starters
  - Vegetarian starters
  - Non-vegetarian starters
- Main Course
  - Vegetarian main courses
  - Non-vegetarian main courses
- Bread / Rice
- Desserts
- Drinks

Each menu item contains:

- Item index
- Item name
- Item price

These properties are represented using the `FoodItem` class.

---

### 2. Order Management

The `Order` class manages the customer's current order.

The system can:

- Add items to the order.
- Add multiple quantities of an item.
- Detect if an item already exists in the order.
- Increase the quantity instead of creating a duplicate cart entry.
- Calculate the total order value.
- Display an order summary.
- Clear the order after successful checkout.

For example, if a customer orders:

```text
Paneer Tikka × 2
Paneer Tikka × 3
```

the cart will contain:

```text
Paneer Tikka × 5
```

rather than two separate entries.

---

### 3. Quantity Validation

The system checks that the requested quantity is greater than zero.

Invalid quantities are rejected instead of being added to the order.

---

### 4. Input Validation

The application uses `try/except` blocks to handle invalid numeric input.

For example, if the program expects:

```text
1
2
3
```

and the user enters:

```text
abc
```

the program displays an error message instead of crashing.

---

### 5. Cart / Order Summary

The customer can view the current order.

The order summary displays:

- Item number
- Food name
- Quantity
- Total price for that item
- Overall bill amount

Example:

```text
Your Order :
------------------------------------------------------------

1 . Paneer tikka x 2 - ₹ 500
2 . Biryani x 1 - ₹ 160
3 . Blueberry cheesecake x 1 - ₹ 140

------------------------------------------------------------
Total : ₹800
```

---

### 6. Bill Generation

The system calculates each item's total using:

```text
item price × quantity
```

The total bill is then calculated by adding the totals of all ordered items.

---

### 7. Checkout

The checkout process:

1. Checks whether the cart is empty.
2. Displays the current order.
3. Asks the customer for confirmation.
4. Confirms the order if the customer enters `yes`.
5. Displays the amount paid.
6. Clears the order after successful checkout.

If the customer enters anything other than `yes`, the order is cancelled and remains in the cart.

---

# 🏗️ Project Structure

The current project is implemented as a Python program.

A recommended future structure is:

```text
restaurant-management-system/
│
├── README.md
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── food_item.py
│   └── order.py
│
├── menu/
│   ├── __init__.py
│   └── menu_data.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── queries.py
│
├── gui/
│   ├── __init__.py
│   └── app.py
│
├── services/
│   ├── __init__.py
│   ├── order_service.py
│   └── billing_service.py
│
├── requirements.txt
│
└── .gitignore
```

> The current project does not yet require this complete structure. It is a recommended architecture for the future SQL + Tkinter version.

---

# 🧱 Current OOP Design

## `FoodItem`

The `FoodItem` class represents an individual food item.

It stores:

```python
index
name
price
```

Conceptually:

```text
FoodItem
   │
   ├── index
   ├── name
   └── price
```

The current implementation initializes these properties in the constructor.

---

## `Order`

The `Order` class represents a customer's current order.

It contains:

```python
items
```

The `items` list stores the food objects and their quantities.

An order entry has the conceptual structure:

```text
{
    "food": FoodItem,
    "quantity": number
}
```

The class currently provides methods for:

- Adding items
- Calculating the bill
- Displaying the order
- Checking out

---

## `take_order()`

`take_order()` acts as a helper function for selecting an item from a displayed menu.

It:

1. Requests an item number.
2. Searches the provided menu.
3. Requests a quantity.
4. Validates the quantity.
5. Adds the item to the `Order`.

This avoids duplicating the same item-selection logic across every menu category.

---

# 🔄 Application Flow

The current application follows this general flow:

```text
                    ┌───────────────┐
                    │     Start     │
                    └───────┬───────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Display Main Menu │
                  └─────────┬─────────┘
                            │
          ┌─────────────────┼──────────────────┐
          │                 │                  │
          ▼                 ▼                  ▼
      Starters         Main Course        Bread/Rice
          │                 │                  │
          └─────────────────┼──────────────────┘
                            │
          ┌─────────────────┼──────────────────┐
          │                 │                  │
          ▼                 ▼                  ▼
       Desserts           Drinks           View Cart
          │                 │                  │
          └─────────────────┼──────────────────┘
                            │
                            ▼
                       Generate Bill
                            │
                            ▼
                         Checkout
                            │
                  ┌─────────┴─────────┐
                  │                   │
                  ▼                   ▼
               Confirm             Cancel
                  │                   │
                  ▼                   │
             Clear Order              │
                  │                   │
                  └─────────┬─────────┘
                            ▼
                     Return to Menu
                            │
                            ▼
                           Exit
```

---

# 💻 Requirements

## Current Version

The current console version requires:

- Python 3.x

No external Python libraries are required for the current console implementation.

You can verify Python with:

```bash
python3 --version
```

---

# ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd restaurant-management-system
```

Run the Python program:

```bash
python3 main.py
```

If the current program is stored under another filename, replace `main.py` with that filename.

---

# 🧪 Example Usage

When the application starts, the user receives a menu similar to:

```text
1. Starter
2. Main Course
3. Bread / Rice
4. Dessert
5. Drinks
6. View cart
7. Generate Bill
8. Checkout
9. Exit
```

The user can select a category and then select a food item.

For example:

```text
Starter
    ↓
Vegetarian
    ↓
Paneer tikka
    ↓
Quantity: 2
    ↓
Added 2 x Paneer tikka to your order.
```

The item can later be viewed in the cart and included in the bill.

---

# 🗄️ Planned SQL Integration

The next major development stage is integrating the application with a SQL database.

Currently, menu items are created directly inside Python functions. This means the data is hard-coded and is not persistent.

For example, the current application creates objects similar to:

```python
FoodItem(1, "Paneer tikka", 250)
```

With SQL integration, this information can instead come from a database.

---

## Proposed Database

MySQL is a suitable choice for the planned version.

A possible database design is:

```text
Restaurant Database
│
├── categories
│
├── menu_items
│
├── customers
│
├── orders
│
└── order_items
```

---

## `categories`

Stores restaurant food categories.

Possible fields:

```text
category_id
category_name
```

Example categories:

```text
1  Starters
2  Main Course
3  Bread / Rice
4  Desserts
5  Drinks
```

---

## `menu_items`

Stores individual food items.

Possible fields:

```text
item_id
category_id
item_name
item_type
price
available
```

Where `item_type` can represent:

```text
Veg
Non-Veg
```

The `available` field can be used to mark an item as currently available or unavailable without deleting it.

---

## `customers`

A future version can store customer information.

Possible fields:

```text
customer_id
customer_name
phone
email
```

Customer information is not currently implemented in the console version.

---

## `orders`

Stores information about each completed order.

Possible fields:

```text
order_id
customer_id
order_date
total_amount
status
```

Possible order statuses:

```text
Pending
Confirmed
Completed
Cancelled
```

---

## `order_items`

Stores the individual food items belonging to an order.

Possible fields:

```text
order_item_id
order_id
item_id
quantity
unit_price
subtotal
```

This creates a relationship between orders and menu items.

---

# 🔗 Proposed Database Relationship

The future database can follow this relationship:

```text
categories
     │
     │ 1
     │
     │
     │ N
menu_items
     │
     │
     │
     │ N
order_items
     │
     │ N
     │
     │ 1
orders
     │
     │ N
     │
     │ 1
customers
```

This design allows the same menu item to appear in many different orders while keeping the menu information centralized.

---

# 🖥️ Planned Tkinter GUI

The current application uses the terminal for all interaction.

The future version will use **Tkinter** to provide a graphical interface.

Possible GUI screens include:

```text
┌────────────────────────────────────────────┐
│          RESTAURANT MANAGEMENT             │
├────────────────────────────────────────────┤
│                                            │
│  [ Starters ]  [ Main Course ]             │
│                                            │
│  [ Bread/Rice ] [ Desserts ] [ Drinks ]    │
│                                            │
│                                            │
│                         [ View Cart ]       │
│                         [ Generate Bill ]   │
│                         [ Checkout ]        │
│                                            │
└────────────────────────────────────────────┘
```

---

## Planned GUI Features

### Menu Screen

Display:

- Food categories
- Food names
- Prices
- Veg/non-veg information
- Availability

### Cart Screen

Display:

- Selected items
- Quantities
- Individual subtotals
- Total amount
- Remove item option
- Quantity update option

### Checkout Screen

Display:

- Order summary
- Total amount
- Customer information
- Confirmation button

### Admin Features — Future Scope

A future administrative interface could allow authorized users to:

- Add menu items.
- Update prices.
- Remove menu items.
- Mark food as available/unavailable.
- View orders.
- Search orders.
- View sales information.

These features are **not currently implemented**.

---

# 🧩 Recommended Future Architecture

When SQL and Tkinter are added, the application should be separated into layers.

```text
┌─────────────────────────┐
│       Tkinter GUI       │
│     Presentation Layer  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Service Layer      │
│   Business Logic        │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     Database Layer      │
│     MySQL / SQL         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       SQL Database      │
└─────────────────────────┘
```

This separation will make the project easier to:

- Maintain
- Debug
- Test
- Expand
- Connect to different interfaces
- Modify without rewriting the entire application

---

# 🔐 Database Security Considerations

When SQL is added, database credentials should **not** be hard-coded into the Python source code.

Avoid:

```python
password = "my_database_password"
```

Instead, use environment variables or a configuration system.

The `.gitignore` file should also prevent sensitive configuration files from being committed to GitHub.

Example:

```text
.env
__pycache__/
*.pyc
```

Never commit real database passwords or API keys to a public repository.

---

# 📊 Future Data Analytics

Because the project is planned to use SQL, it can eventually be expanded into a small restaurant analytics system.

Possible analytics include:

### Sales Analysis

- Total sales
- Daily sales
- Weekly sales
- Monthly sales

### Item Analysis

- Most ordered food
- Least ordered food
- Most profitable items
- Category-wise sales

### Customer Analysis

- Number of orders
- Average order value
- Repeat customers

### Visualization

The project could eventually use Python libraries such as:

```text
Pandas
Matplotlib
```

to generate charts from SQL data.

For example:

```text
Monthly Sales
     │
     │       █
     │   █   █
     │   █   █       █
     │ █ █   █   █   █
     └──────────────────
       Jan Feb Mar Apr
```

This would make the project more relevant to **data analytics and data science** as well as software development.

---

# 🚧 Current Limitations

The current console implementation has several limitations.

### 1. No persistent storage

Orders and menu information exist only while the Python program is running.

### 2. Hard-coded menu

Food items are currently defined directly in Python.

### 3. No graphical interface

The application currently runs through the terminal.

### 4. No customer database

Customer details are not currently stored.

### 5. No order history

Previous completed orders are cleared from memory after checkout.

### 6. No authentication

There is currently no customer/admin login system.

### 7. No inventory management

The application does not currently track ingredient or food stock.

### 8. No tax/discount system

The current bill calculates item prices and quantities but does not implement taxes, discounts, service charges, or other billing rules.

---

# 🛠️ Future Roadmap

## Phase 1 — Console Application

- [x] Create `FoodItem` class
- [x] Create `Order` class
- [x] Add menu categories
- [x] Add quantity handling
- [x] Add cart functionality
- [x] Add bill calculation
- [x] Add checkout
- [x] Add input validation

## Phase 2 — Code Refactoring

- [ ] Separate classes into modules
- [ ] Create centralized menu data
- [ ] Improve error handling
- [ ] Add unit tests
- [ ] Improve naming and documentation
- [ ] Add better exception handling

## Phase 3 — SQL Integration

- [ ] Install/configure MySQL
- [ ] Create restaurant database
- [ ] Create database tables
- [ ] Connect Python to MySQL
- [ ] Store menu items in SQL
- [ ] Retrieve menu items from SQL
- [ ] Store customer information
- [ ] Store orders
- [ ] Store order items
- [ ] Retrieve previous orders
- [ ] Add database CRUD operations

## Phase 4 — Tkinter GUI

- [ ] Create main window
- [ ] Create category navigation
- [ ] Display menu items
- [ ] Add items to cart through GUI
- [ ] Create cart window
- [ ] Add quantity controls
- [ ] Create checkout interface
- [ ] Display generated bill
- [ ] Connect GUI to service layer

## Phase 5 — Advanced Features

- [ ] Admin dashboard
- [ ] Customer accounts
- [ ] Order history
- [ ] Search functionality
- [ ] Menu availability
- [ ] Discounts
- [ ] Taxes/service charges
- [ ] Inventory management
- [ ] Sales analytics
- [ ] Data visualization

---

# 🧪 Testing Plan

The project should eventually include tests for important operations.

Examples:

### Food Item

Verify that:

- Food name is stored correctly.
- Price is stored correctly.
- Index is stored correctly.

### Order

Verify that:

- Items can be added.
- Quantities are correctly stored.
- Repeated items increase quantity.
- Bill calculations are correct.
- Empty orders are handled correctly.
- Checkout clears the order after confirmation.

### Input Validation

Test:

```text
abc
-1
0
1
999
```

to ensure invalid inputs are handled properly.

### Database

After SQL integration, test:

- Insert
- Select
- Update
- Delete
- Foreign-key relationships
- Invalid database input
- Connection failures

---

# 📚 Concepts Demonstrated

This project currently demonstrates several Python programming concepts:

- Object-Oriented Programming
- Classes and objects
- Constructors
- Instance attributes
- Lists
- Dictionaries
- Loops
- Conditional statements
- Functions
- Function arguments
- `for` loops
- `while` loops
- `enumerate()`
- Exception handling
- `try/except`
- User input
- String formatting
- Basic data modelling

Future versions will additionally demonstrate:

- SQL
- Database normalization
- CRUD operations
- Database connectivity
- GUI programming
- Software architecture
- Data analytics
- Data visualization

---

# 🤝 Contributing

Contributions and improvements are welcome.

A suggested workflow is:

```bash
git checkout -b feature/new-feature
```

Make your changes, test them, and then commit:

```bash
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

Then create a pull request on GitHub.

---

# 📄 License

This project is intended primarily as an educational/project-work application.

If you plan to distribute the project publicly, add an appropriate open-source license such as MIT and update this section accordingly.

---

# 👨‍💻 Author

**Arijit Shaw**

This project is being developed as a learning project to practice:

- Python
- Object-Oriented Programming
- SQL
- GUI development
- Database management
- Data analytics

---

# ⭐ Project Vision

The long-term goal of this project is to evolve from a simple console-based restaurant ordering program into a complete desktop restaurant management application:

```text
                CURRENT
                   │
                   ▼
        ┌────────────────────┐
        │ Python Console App │
        └─────────┬──────────┘
                  │
                  ▼
             SQL Database
                  │
                  ▼
           Tkinter Interface
                  │
                  ▼
        Restaurant Management
             Application
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Orders     Menu     Customers
        │         │         │
        └─────────┼─────────┘
                  ▼
             Analytics
                  │
                  ▼
          Business Insights
```

The project is therefore designed not just as a basic ordering program, but as a foundation that can later incorporate **database management, GUI development, and data analytics**.
