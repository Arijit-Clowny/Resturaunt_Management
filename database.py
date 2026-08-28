import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


# -------- DATABASE CONNECTION --------

def get_connection():

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


# -------- GET FOOD ITEMS --------

def get_food_items(category, food_type=None):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT food_id, name, price, category, food_type
    FROM food_items
    WHERE category = %s
    """

    values = (category,)

    if food_type:
        query += " AND food_type = %s"
        values += (food_type,)

    cursor.execute(query, values)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

def food_items_from_db(category, food_type=None):
    rows = get_food_items(category, food_type)
    return rows