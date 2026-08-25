import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(host = os.getenv("DB_HOST"),user = os.getenv("DB_USER"),password = os.getenv("DB_PASSWORD"),database = os.getenv("DB_NAME"))

cursor = connection.cursor()

# Gets menu from Mysql.

def get_food_items(category , food_type = None):

    query = """
    SELECT food_id, name, price, category, food_type
    FROM food_items
    WHERE category = %s
    """

    values = (category,)

    if food_type:
        query += "AND food_type = %s"
        values += (food_type,)

    cursor.execute(query , values)

    return cursor.fetchall()

# Converts the menu in FoodItem objects.

def food_items_from_db(category , food_type = None):

    rows = get_food_items(category , food_type)

    return rows

# Save orders in Mysql.

def create_order(subtotal , gst , total):

    query = """
    INSERT INTO orders (subtotal, gst, total)
    VALUES (%s, %s, %s)
    """

    values = (subtotal, gst, total)

    cursor.execute(query, values)

    return cursor.lastrowid

# Add order items into order.

def add_order_item(order_id, food_id, quantity, price):

    query = """
    INSERT INTO order_items
    (order_id, food_id, quantity, price)
    VALUES (%s, %s, %s, %s)
    """

    values = (order_id, food_id, quantity, price)

    cursor.execute(query, values)