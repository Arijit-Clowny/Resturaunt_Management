import tkinter as tk
from tkinter import messagebox
from decimal import Decimal
from config import *


#--------CART-------

cart = []

# --------SHOW CART---------

def show_cart(menu_frame, place_order , order_success=None):

    for widget in menu_frame.winfo_children():
        widget.destroy()

    heading = tk.Label(
        menu_frame,
        text="YOUR CART",
        font=SECTION_FONT,
        bg=CARD,
        fg=TEXT
    )

    heading.pack(pady=(0, 15))

    subtotal = Decimal("0.00")

    if not cart:
        empty_label = tk.Label(
            menu_frame,
            text="Your cart is empty.",
            font=("Arial", 15),
            bg=CARD,
            fg=SECONDARY_TEXT
        )
        empty_label.pack(pady=20)
        return

    # -------- CART ITEMS --------

    for order in cart:

        item = order["food"]
        quantity = order["quantity"]

        item_total = item.price * quantity
        subtotal += item_total

        cart_label = tk.Label(
            menu_frame,
            text=f"{item.name:30}  x {quantity:3}  ₹ {item_total:8.2f}",
            font=("Courier New", 13, "bold"),
            bg=CARD,
            fg=TEXT
        )

        cart_label.pack(anchor="w", pady=3)

    # -------- BILL --------

    gst = subtotal * Decimal("0.18")
    total = subtotal + gst

    separator = tk.Label(
        menu_frame,
        text="-" * 55,
        font=("Courier New", 12),
        bg=CARD,
        fg=BORDER
    )

    separator.pack(pady=(10, 5))

    subtotal_label = tk.Label(
        menu_frame,
        text=f"Subtotal:                              ₹ {subtotal:8.2f}",
        font=("Courier New", 13, "bold"),
        bg=CARD,
        fg=TEXT
    )

    subtotal_label.pack(anchor="w")

    gst_label = tk.Label(
        menu_frame,
        text=f"GST (18%):                             ₹ {gst:8.2f}",
        font=("Courier New", 13, "bold"),
        bg=CARD,
        fg=TEXT
    )

    gst_label.pack(anchor="w")

    total_label = tk.Label(
        menu_frame,
        text=f"TOTAL:                           ₹ {total:8.2f}",
        font=("Courier New", 15, "bold"),
        bg=CARD,
        fg=ACCENT
    )

    total_label.pack(anchor="w", pady=(5, 0))

    def checkout():
        try:
            result = place_order(cart)

            if result is None:
                messagebox.showwarning(
                    "Empty Cart",
                    "Your cart is empty."
                )
                return

            order_id, total = result

            cart.clear()

            if order_success:
                order_success()

            messagebox.showinfo(
                "Order Placed",
                f"Your order has been placed successfully!\n\n"
                f"Order ID: {order_id}\n"
                f"Total: ₹ {total:.2f}"
            )

            show_cart(menu_frame, place_order, order_success)

        except Exception as error:

            messagebox.showerror(
                "Order Failed",
                f"Could not place the order.\n\n{error}"
            )

    place_order_button = tk.Button(
        menu_frame,
        text="PLACE ORDER",
        command=checkout,
        font=BUTTON_FONT,
        bg=ACCENT,
        fg="black",
        activebackground=HEADER,
        activeforeground="white",
        relief="flat",
        bd=0,
        width=20,
        height=2,
        cursor="hand2"
    )

    place_order_button.pack(pady=(20, 5))

    #---------Quantity control----------

def create_quantity_control(parent, item):

    quantity = tk.IntVar(value=0)

    for order in cart:
        if order["food"].name == item.name:      # <-- match by name
            quantity.set(order["quantity"])
            break

    def increase():
        quantity.set(quantity.get() + 1)

        for order in cart:
            if order["food"].name == item.name:  # <-- match by name
                order["quantity"] = quantity.get()
                break
        else:
            cart.append({"food": item, "quantity": quantity.get()})
        update_quantity()

    def decrease():
        if quantity.get() > 0:
            quantity.set(quantity.get() - 1)
            for order in cart:
                if order["food"].name == item.name:   # <-- match by name
                    order["quantity"] = quantity.get()
                    if order["quantity"] == 0:
                        cart.remove(order)
                    break
            update_quantity()

    def update_quantity(*args):
        if quantity.get() == 0:
            quantity_label.config(text="")
            minus_button.grid_remove()
        else:
            quantity_label.config(text=str(quantity.get()))
            minus_button.grid(row=0, column=0, padx=(3, 0))

    item_frame = tk.Frame(parent, bg=CARD)
    item_frame.pack(fill="x", pady=3)

    item_label = tk.Label(
        item_frame,
        text=f"{item.name:<30} ₹ {item.price:8.2f}",
        font=("Courier New", 13, "bold"),
        bg=CARD,
        fg=TEXT
    )
    item_label.pack(side="left")

    quantity_frame = tk.Frame(item_frame, bg=CARD, width=180, height=30)
    quantity_frame.pack(side="right")
    quantity_frame.pack_propagate(False)

    minus_button = tk.Button(
        quantity_frame,
        text="-",
        width=2,
        command=decrease
    )
    # not gridded yet — starts hidden since quantity is 0

    quantity_label = tk.Label(
        quantity_frame,
        text="",
        width=3,
        font=("Courier New", 12, "bold"),
        bg=CARD,
        fg=TEXT
    )
    quantity_label.grid(row=0, column=1, padx=3)

    plus_button = tk.Button(
        quantity_frame,
        text="+",
        width=2,
        command=increase
    )
    plus_button.grid(row=0, column=2)

    update_quantity()