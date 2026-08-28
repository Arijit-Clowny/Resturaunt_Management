from models import *
from database import *

# Converts tuples from database rows to FoodItem object.

def get_food_objects(category, food_type=None):

    rows = food_items_from_db(category, food_type)

    food_items = []

    for row in rows:
        food = FoodItem(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )

        food_items.append(food)

    return food_items
