class FoodItem:

    #initialize FoodItems with item name and price.

    def __init__(self,index,name,price):
        self.index = index
        self.name = name    
        self.price = price  

class Order:

    # Initialize order with empty list.

    def __init__(self):
        self.items = []

    # Initialize food to order with quantity.

    def add_items(self,food,quantity):

        for item in self.items:
            if item["food"].name == food.name:
                item["quantity"] += quantity
                print(f"Added {quantity} more {food.name} to your order.\n")
                return
            
        self.items.append({"food" : food, "quantity" : quantity})
        print(f"Added {quantity} x {food.name} to your order.\n")

    # Calculate total price of the order.

    def bill(self):

        total = 0

        for item in self.items:
            food = item["food"]
            quantity = item["quantity"]

            total += food.price * quantity

        return total

    # Show order sumary.

    def show_orders(self):

        if not self.items:
            print("No items in the order.\n")
            return
        
        print("\nYour Order : \n")
        print("-" * 42)

        for i,item in enumerate(self.items, start = 1):

            food = item["food"]
            quantity = item["quantity"]

            item_total = food.price * quantity

            print(f"{i} . {food.name:<25} "f"x {quantity} - "f"₹ {item_total}")

        print("-" * 42)
        print("GST : "," " * 25,f"₹{self.bill() * 0.18 :.3f}")
        print("Total : "," "*23,f"₹{self.bill() + (self.bill() * 0.18 ):.2f}\n")

    # Remove n items from cart.

    def remove_item(self):

        if not self.items:
            print("Your cart is empty.\n")
            return

        self.show_orders()

        try:

            choice = int(input("Enter the item number you want to remove.\n"))

            if choice < 1 or choice > len(self.items):
                print("Invalid number.\n")
                return

            item = self.items[choice - 1]
            food = item["food"]
            quantity = item["quantity"]

            remove_quantity = int(input(f"How many {food.name} do you want to remove? \n"))

            if remove_quantity <= 0:
                print("Quantity must be greater than 0\n")
                return

            if remove_quantity > quantity:
                print(f"you have only {quantity} {food.name} in your cart\n")
                return

            item["quantity"] -= remove_quantity

            if item["quantity"] == 0:
                self.items.pop(choice - 1)
                print(f"All {food.name} removed from your cart.\n")

            else:
                print(f"Removed {remove_quantity} {food.name} from your cart.\n")

        except ValueError:
            print("Please enter a valid number.\n")

    # Handel checkout process.

    def checkout(self):

        if not self.items:
            print("Your cart is empty.\n")
            return
        
        self.show_orders()

        confirm = input("Proceed to checkout ? (yes/no)\n").strip().lower()

        if confirm == "yes":
            print("\nOrder confirmed!!")
            sub_total = self.bill()
            gst = sub_total * 0.18
            total = sub_total + gst
            print(f"Amount paid : ₹{total:.2f}")
            print("Thank you.")
            self.items.clear()

        else:
            print("Order cancelled.\n")
