import tkinter as tk
from PIL import Image, ImageTk

from menu import get_food_objects
from cart import create_quantity_control, show_cart
from config import *
from order_service import place_order
from database import get_order_history


class ResturantApp:

    # --------- INITIALIZE APPLICATION ---------

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Restaurant Management System")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{screen_width}x{screen_height}"
        )

        # --------- BACKGROUND ---------

        background_image = Image.open(
            "assets/resturant.jpeg"
        )

        background_image = background_image.resize(
            (screen_width, screen_height)
        )

        self.background_photo = ImageTk.PhotoImage(
            background_image
        )

        self.background_label = tk.Label(
            self.root,
            image=self.background_photo
        )

        self.background_label.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # --------- HEADER ---------

        self.create_header()

        # --------- CATEGORY FRAME ---------

        self.create_category_frame()

        # --------- MENU FRAME ---------

        self.menu_frame = tk.Frame(
            self.root,
            bg=CARD,
            padx=30,
            pady=20
        )

        self.menu_frame.pack(
            pady=10
        )

        self.background_label.lower()

    # --------- HEADER ---------

    def create_header(self):

        self.header = tk.Frame(
            self.root,
            bg=HEADER,
            height=150
        )

        self.header.pack(
            fill="x",
            side="top"
        )

        self.header.pack_propagate(False)

        title = tk.Label(
            self.header,
            text="🍽️ RESTAURANT MANAGEMENT SYSTEM",
            font=TITLE_FONT,
            bg=HEADER,
            fg="white"
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = tk.Label(
            self.header,
            text="Good food, Great moments.",
            font=SUBTITLE_FONT,
            bg=HEADER,
            fg="#D8CEC4"
        )

        subtitle.pack()

    # --------- CATEGORY FRAME ---------

    def create_category_frame(self):

        self.category_frame = tk.Frame(
            self.root,
            bg=CARD,
            padx=50,
            pady=25
        )

        self.category_frame.pack(
            pady=30
        )

        category_title = tk.Label(
            self.category_frame,
            text="What would you like to have?",
            font=SECTION_FONT,
            bg=CARD,
            fg=TEXT
        )

        category_title.grid(
            row=0,
            column=0,
            columnspan=6,
            pady=(0, 20)
        )

        # --------- BUTTONS ---------

        starter_button = tk.Button(
            self.category_frame,
            text="🥗\nStarters",
            command=self.show_starters,
            font=BUTTON_FONT,
            bg=CARD,
            fg=TEXT,
            activebackground=ACCENT,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        main_course_button = tk.Button(
            self.category_frame,
            text="🍛\nMain Courses",
            command=self.show_main_courses,
            font=BUTTON_FONT,
            bg=CARD,
            fg=TEXT,
            activebackground=ACCENT,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        bread_rice_button = tk.Button(
            self.category_frame,
            text="🍚\nBread / Rice",
            command=self.show_bread_rice,
            font=BUTTON_FONT,
            bg=CARD,
            fg=TEXT,
            activebackground=ACCENT,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        dessert_button = tk.Button(
            self.category_frame,
            text="🍰\nDesserts",
            command=self.show_desserts,
            font=BUTTON_FONT,
            bg=CARD,
            fg=TEXT,
            activebackground=ACCENT,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        drinks_button = tk.Button(
            self.category_frame,
            text="🥤\nDrinks",
            command=self.show_drinks,
            font=BUTTON_FONT,
            bg=CARD,
            fg=TEXT,
            activebackground=ACCENT,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        cart_button = tk.Button(
            self.category_frame,
            text="🛒\nView Cart",
            command=self.view_cart,
            font=BUTTON_FONT,
            bg=ACCENT,
            fg="black",
            activebackground=HEADER,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        # --------- BUTTON POSITION ---------

        starter_button.grid(
            row=1,
            column=0,
            padx=10
        )

        main_course_button.grid(
            row=1,
            column=1,
            padx=10
        )

        bread_rice_button.grid(
            row=1,
            column=2,
            padx=10
        )

        dessert_button.grid(
            row=1,
            column=3,
            padx=10
        )

        drinks_button.grid(
            row=1,
            column=4,
            padx=10
        )

        cart_button.grid(
            row=1,
            column=5,
            padx=10
        )

        # --------- HOVER ---------

        self.button_hover(starter_button)
        self.button_hover(main_course_button)
        self.button_hover(bread_rice_button)
        self.button_hover(dessert_button)
        self.button_hover(drinks_button)
        self.button_hover(cart_button)

    # --------- BUTTON HOVER ---------

    def button_hover(self, button):

        def on_enter(event):

            button.config(
                bg=ACCENT,
                fg="orange"
            )

        def on_leave(event):

            button.config(
                bg=CARD,
                fg=TEXT
            )

        button.bind(
            "<Enter>",
            on_enter
        )

        button.bind(
            "<Leave>",
            on_leave
        )

    # --------- CLEAR MENU FRAME ---------

    def clear_menu(self):

        for widget in self.menu_frame.winfo_children():
            widget.destroy()

    # --------- STARTERS ---------

    def show_starters(self):

        self.clear_menu()

        veg_items = get_food_objects(
            "Starter",
            "Veg"
        )

        non_veg_items = get_food_objects(
            "Starter",
            "Non-Veg"
        )

        heading = tk.Label(
            self.menu_frame,
            text="STARTERS",
            font=SECTION_FONT,
            bg=CARD,
            fg=TEXT
        )

        heading.pack(
            pady=(0, 10)
        )

        veg_heading = tk.Label(
            self.menu_frame,
            text="🥗 Vegetarian",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        veg_heading.pack(
            anchor="w"
        )

        for item in veg_items:

            create_quantity_control(
                self.menu_frame,
                item
            )

        non_veg_heading = tk.Label(
            self.menu_frame,
            text="🍗 Non-Vegetarian",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        non_veg_heading.pack(
            anchor="w",
            pady=(15, 0)
        )

        for item in non_veg_items:

            create_quantity_control(
                self.menu_frame,
                item
            )

    # --------- MAIN COURSE ---------

    def show_main_courses(self):

        self.clear_menu()

        veg_items = get_food_objects(
            "Main Course",
            "Veg"
        )

        non_veg_items = get_food_objects(
            "Main Course",
            "Non-Veg"
        )

        heading = tk.Label(
            self.menu_frame,
            text="MAIN COURSE",
            font=SECTION_FONT,
            bg=CARD,
            fg=TEXT
        )

        heading.pack(
            pady=(0, 10)
        )

        veg_heading = tk.Label(
            self.menu_frame,
            text="🥗 Vegetarian",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        veg_heading.pack(
            anchor="w"
        )

        for item in veg_items:

            create_quantity_control(
                self.menu_frame,
                item
            )

        non_veg_heading = tk.Label(
            self.menu_frame,
            text="🍗 Non-Vegetarian",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        non_veg_heading.pack(
            anchor="w",
            pady=(15, 0)
        )

        for item in non_veg_items:

            create_quantity_control(
                self.menu_frame,
                item
            )

    # --------- BREAD / RICE ---------

    def show_bread_rice(self):

        self.clear_menu()

        items = get_food_objects(
            "Bread/Rice"
        )

        heading = tk.Label(
            self.menu_frame,
            text="BREAD / RICE",
            font=SECTION_FONT,
            bg=CARD,
            fg=TEXT
        )

        heading.pack(
            pady=(0, 10)
        )

        bread_rice_heading = tk.Label(
            self.menu_frame,
            text="🍞/🍚 Bread/Rice",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        bread_rice_heading.pack(
            anchor="w"
        )

        for item in items:

            create_quantity_control(
                self.menu_frame,
                item
            )

    # --------- DESSERTS ---------

    def show_desserts(self):

        self.clear_menu()

        items = get_food_objects(
            "Dessert"
        )

        heading = tk.Label(
            self.menu_frame,
            text="DESSERT",
            font=SECTION_FONT,
            bg=CARD,
            fg=TEXT
        )

        heading.pack(
            pady=(0, 10)
        )

        dessert_heading = tk.Label(
            self.menu_frame,
            text="🍨 Dessert",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        dessert_heading.pack(
            anchor="w"
        )

        for item in items:

            create_quantity_control(
                self.menu_frame,
                item
            )

    # --------- DRINKS ---------

    def show_drinks(self):

        self.clear_menu()

        items = get_food_objects(
            "Drinks"
        )

        heading = tk.Label(
            self.menu_frame,
            text="DRINKS",
            font=SECTION_FONT,
            bg=CARD,
            fg=TEXT
        )

        heading.pack(
            pady=(0, 10)
        )

        drinks_heading = tk.Label(
            self.menu_frame,
            text="🥤 Drinks",
            font=BUTTON_FONT,
            bg=CARD,
            fg=ACCENT
        )

        drinks_heading.pack(
            anchor="w"
        )

        for item in items:

            create_quantity_control(
                self.menu_frame,
                item
            )

    # --------- VIEW CART ---------

    def view_cart(self):

        show_cart(
            self.menu_frame,
            place_order,
            self.create_history_button
        )
    # ---------ORDER HISTORY----------

    # --------- ORDER HISTORY ----------

    def view_history(self):
        self.clear_menu()
        orders = get_order_history()

        heading = tk.Label(
            self.menu_frame, text="ORDER HISTORY", font=SECTION_FONT, bg=CARD, fg=TEXT
        )
        heading.pack(pady=(0, 20))

        if not orders:
            tk.Label(
                self.menu_frame, text="No orders found.", font=BUTTON_FONT, bg=CARD, fg=TEXT
            ).pack()
            return

        # --------- GROUP ORDERS ---------
        grouped_orders = {}

        for row in orders:
            (order_id, order_date, subtotal, gst, total,
             food_name, quantity, item_price) = row

            if order_id not in grouped_orders:
                grouped_orders[order_id] = {
                    "date": order_date,
                    "subtotal": subtotal,
                    "gst": gst,
                    "total": total,
                    "items": []
                }

            grouped_orders[order_id]["items"].append((food_name, quantity, item_price))

        # --------- SCROLLABLE CONTAINER ---------
        history_container = tk.Frame(self.menu_frame, bg=CARD)
        history_container.pack(fill="both", expand=True)

        # --------- CANVAS ---------
        canvas = tk.Canvas(history_container, bg=CARD, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        # --------- SCROLLBAR ---------
        scrollbar = tk.Scrollbar(history_container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # --------- FRAME INSIDE CANVAS ---------
        history_frame = tk.Frame(canvas, bg=CARD)
        canvas_window = canvas.create_window((0, 0), window=history_frame, anchor="nw")

        # --------- UPDATE SCROLL REGION ---------
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))

        history_frame.bind("<Configure>", update_scroll_region)

        # --------- MATCH WIDTH ---------
        def update_width(event):
            canvas.itemconfig(canvas_window, width=event.width)

        canvas.bind("<Configure>", update_width)

        # --------- DISPLAY ORDERS ---------
        for order_id, order in grouped_orders.items():
            order_frame = tk.Frame(history_frame, bg="white", padx=20, pady=15)
            order_frame.pack(fill="x", pady=8, padx=5)

            # --------- ORDER ID ---------
            tk.Label(
                order_frame, text=f"Order #{order_id}", font=BUTTON_FONT, bg="white", fg=TEXT
            ).pack(anchor="w")

            # --------- DATE ---------
            tk.Label(
                order_frame, text=f"Date: {order['date']}", bg="white", fg=TEXT
            ).pack(anchor="w")

            # --------- ITEMS ---------
            tk.Label(
                order_frame, text="Items:", font=BUTTON_FONT, bg="white", fg=TEXT
            ).pack(anchor="w",)

            # --------- SUBTOTAL ---------
            tk.Label(
                order_frame, text=f"Subtotal: ₹{order['subtotal']:.2f}", bg="white", fg=TEXT
            ).pack(anchor="w", pady=(10, 0))

            # --------- GST ---------
            tk.Label(
                order_frame, text=f"GST: ₹{order['gst']:.2f}", bg="white", fg=TEXT
            ).pack(anchor="w")

            # --------- TOTAL ---------
            tk.Label(
                order_frame, text=f"Total: ₹{order['total']:.2f}", font=BUTTON_FONT, bg="white", fg=TEXT
            ).pack(anchor="w")

    #-----------HISTORY BUTTON-----------

    def create_history_button(self):

        if hasattr(self, "history_button"):
            return

        self.history_button = tk.Button(
            self.category_frame,
            text="📋\nOrder History",
            command=self.view_history,
            font=BUTTON_FONT,
            bg=ACCENT,
            fg="black",
            activebackground=HEADER,
            activeforeground="white",
            relief="flat",
            bd=0,
            width=14,
            height=4,
            cursor="hand2"
        )

        self.history_button.grid(
            row=1,
            column=6,
            padx=10
        )

        self.button_hover(self.history_button)
    # --------- RUN APPLICATION ---------

    def run(self):

        self.root.mainloop()
