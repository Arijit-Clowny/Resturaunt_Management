from decimal import Decimal
from database import get_connection


# --------- PLACE ORDER ---------

def place_order(cart):

    if not cart:
        return None

    subtotal = Decimal("0.00")

    # -------- CALCULATE BILL --------

    for order in cart:

        item = order["food"]
        quantity = order["quantity"]

        subtotal += item.price * quantity

    gst = subtotal * Decimal("0.18")
    total = subtotal + gst

    conn = None
    cursor = None

    try:

        conn = get_connection()
        cursor = conn.cursor()

        # -------- INSERT ORDER --------

        order_query = """
            INSERT INTO orders
            (order_date, subtotal, gst, total)
            VALUES (NOW(), %s, %s, %s)
        """

        cursor.execute(
            order_query,
            (subtotal, gst, total)
        )

        order_id = cursor.lastrowid

        # -------- INSERT ORDER ITEMS --------

        item_query = """
            INSERT INTO order_items
            (order_id, food_id, quantity, price)
            VALUES (%s, %s, %s, %s)
        """

        for order in cart:

            item = order["food"]
            quantity = order["quantity"]

            cursor.execute(
                item_query,
                (
                    order_id,
                    item.index,
                    quantity,
                    item.price
                )
            )

        # -------- COMMIT --------

        conn.commit()

        return order_id, total

    except Exception:

        if conn:
            conn.rollback()

        raise

    finally:

        if cursor:
            cursor.close()

        if conn:
            conn.close()