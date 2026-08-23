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

            total += food.price * quantity + (0.18 * food.price * quantity)

        return total

    # Show order sumary.

    def show_orders(self):

        if not self.items:
            print("No items in the order.\n")
            return
        
        print("\nYour Order : \n")
        print("-" * 60)

        for i,item in enumerate(self.items, start = 1):

            food = item["food"]
            quantity = item["quantity"]

            item_total = food.price * quantity

            item_gst = 0.18 * food.price * quantity

            print(f"{i} . {food.name} "f"x {quantity} - "f"₹ {item_total}\n")
            print("GST : "f"₹ {item_gst}\n")

        print("-" * 60)
        print(f"Total : ₹{self.bill()}\n")

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
            print(f"Amount paid : ₹{self.bill()}")
            print("Thank you.")
            self.items.clear()

        else:
            print("Order cancelled.\n")

#------------------------------------------------------
# Function to add items from menu and add it to order.
#------------------------------------------------------

def take_order(menu, order):

    try:
        choice = int(input("Enter the item number : \n"))

        for item in menu:

            if item.index == choice:

                quantity = int(input(f"Enter quantity of {item.name}: \n"))

                if quantity <= 0:
                    print("Quantity numst be greater than 0.\n")
                    return
                
                order.add_items(item,quantity)
                return
            
        print("Invalid item number.\n")

    except ValueError:
        print("Please enter a valid number.\n") 

#------------------------------------------------------
# Starters.
#------------------------------------------------------

def starter(order):

    run = True

    while(run):

        try:

            choice2 = int(input("\nEnter :\n1.For veg items.\n2.For non veg items.\n3.Go back.\n\n"))

        except ValueError:

            print("Please enter a valid number.\n")
            continue

        if choice2 == 1:

            vitem1 = FoodItem(1,"Paneer tikka",250)
            vitem2 = FoodItem(2,"Crispy Chilli Baby Corn",200)
            vitem3 = FoodItem(3,"Hara Bhara Kebab",160)
            vitem4 = FoodItem(4,"Veg Manchurian",180)
            vitem5 = FoodItem(5,"Chilli Mushroom",220)

            # Initialize all veg starters in a list.

            lv = [vitem1,vitem2,vitem3,vitem4,vitem5]

            print("\n---- VEG STARTERS ----")

            for i in lv:
                print(i.index,".",i.name," - ₹",i.price)

            # Takes order.

            take_order(lv , order)
    
        elif choice2 == 2:

            nvitem1 = FoodItem(1,"Chicken tikka",300)
            nvitem2 = FoodItem(2,"Chilli Chicken",260)
            nvitem3 = FoodItem(3,"Fish Fingers",280)
            nvitem4 = FoodItem(4,"Chicken 65",240)
            nvitem5 = FoodItem(5,"Mutton Seekh Kebab",380)

            # Initialize all non veg starters in a list.

            lnv = [nvitem1,nvitem2,nvitem3,nvitem4,nvitem5]

            print("\n---- NON-VEG STARTERS ----")

            for i in lnv:
                print(i.index,".",i.name," - ₹",i.price)

            # Takes order.

            take_order(lnv , order)

        elif choice2 == 3:

            run = False
        else:
            print("Wrong choice.\n")

#------------------------------------------------------
# Main courses.
#------------------------------------------------------

def main_course(order):

    run = True

    while(run):

        try:

            choice2 = int(input("\nEnter :\n1.For veg items.\n2.For non veg items.\n3.Go back.\n\n"))

        except ValueError:
    
            print("Please enter a valid number.\n")
            continue

        if choice2 == 1:

            vitem1 = FoodItem(1,"Soya Chunks Masala",180)
            vitem2 = FoodItem(2,"Palak Paneer",280)
            vitem3 = FoodItem(3,"Kadai Paneer",290)
            vitem4 = FoodItem(4,"Dal Tadka",180)
            vitem5 = FoodItem(5,"Vegetable Jalfrezi",240)

            # Initialize all veg main courses in a list.

            lv = [vitem1,vitem2,vitem3,vitem4,vitem5]

            print("\n---- VEG MAIN COURSES ----")

            for i in lv:
                print(i.index,".",i.name," - ₹",i.price)

            take_order(lv , order)

        elif choice2 == 2:

            nvitem1 = FoodItem(1,"Grilled Chicken Breast",400)
            nvitem2 = FoodItem(2,"Chicken Tikka Masala",350)
            nvitem3 = FoodItem(3,"Macher Jhol (Bengali Fish Curry",300)
            nvitem4 = FoodItem(4,"Mutton Rogan Josh",450)
            nvitem5 = FoodItem(5,"Bhuna Gosht",480)

            # Initialize all non veg Main courses in a list.

            lnv = [nvitem1,nvitem2,nvitem3,nvitem4,nvitem5]

            print("\n----NON-VEG MAIN COURSES ----")
            
            for i in lnv:
                print(i.index,".",i.name," - ₹",i.price)
            
            take_order(lnv , order)

        elif choice2 == 3:

            return
        
        else:
            print("Wrong Choice\n.")

#------------------------------------------------------
# Desserts.
#------------------------------------------------------

def dessert(order):

    run = True
        
    while(run):
        
        try:
        
            choice2 = int(input("\nEnter :\n1.To order.\n2.Go back.\n\n"))
        
        except ValueError:
            
            print("Please enter a valid number.\n")
            continue

        if choice2 == 1:
            item1 = FoodItem(1,"Ice cream",110)
            item2 = FoodItem(2,"Brownie",120)
            item3 = FoodItem(3,"Gulab jamun with ice cream",160)
            item4 = FoodItem(4,"Blueberry cheesecake",140)
            item5 = FoodItem(5,"Rabdi jalebi",120)
    
            # Initialize all desserte in a list.
    
            l = [item1,item2,item3,item4,item5]

            print("\n---- DESSERTS ----")
    
            for i in l:
                print(i.index,".",i.name," - ₹",i.price)

            take_order(l , order)

        elif choice2 == 2:
        
            return

        else:

            print("Wrong choice.\n")

#------------------------------------------------------
# Bread / Rice.
#------------------------------------------------------

def bread_rice(order):

    run = True
            
    while(run):
            
        try:
            
            choice2 = int(input("\nEnter :\n1.To order.\n2.Go back.\n\n"))
            
        except ValueError:
                
            print("Please enter a valid number.\n")
            continue
    
        if choice2 == 1:

            item1 = FoodItem(1,"Butter Naan",30)
            item2 = FoodItem(2,"Naan",20)
            item3 = FoodItem(3,"Tawa roti",10)
            item4 = FoodItem(4,"jeera rice",100)
            item5 = FoodItem(5,"Biryani",160)
            item6 = FoodItem(6,"Fried rice (veg)",150)

            # Initialize all breads / rice items in a list.

            l = [item1,item2,item3,item4,item5,item6]

            print("\n---- BREAD / RICE ----")
        
            for i in l:
                print(i.index,".",i.name," - ₹",i.price)

            take_order(l , order)

        elif choice2 == 2:
                
            return
        
        else:
        
            print("Wrong choice.\n")
        

#------------------------------------------------------
# Drinks.
#------------------------------------------------------

def Drinks(order):

    run = True
                
    while(run):
                
        try:
                
            choice2 = int(input("\nEnter :\n1.To order.\n2.Go back.\n\n"))
                
        except ValueError:
                    
            print("Please enter a valid number.\n")
            continue
        
        if choice2 == 1:

            item1 = FoodItem(1,"Cold drinks",90)
            item2 = FoodItem(2,"Virgin Mojito",120)
            item3 = FoodItem(3,"Blue lagoon",120)
            item4 = FoodItem(4,"Lemonade",110)
            item5 = FoodItem(5,"Lassi",90)
        
            # Initialize all Drinks in a list.
        
            l = [item1,item2,item3,item4,item5]

            print("\n---- DRINKS ----")
        
            for i in l:
                print(i.index,".",i.name," - ₹",i.price)

            take_order(l , order)

        elif choice2 == 2:
                        
            return
                
        else:
                
            print("Wrong choice.\n")

#------------------------------------------------------
# Main Function.
#------------------------------------------------------
    
def main():

    # One order object for the entire program.
    order = Order()

    print("=" * 70)
    print("\t" * 3, "MENU")
    print("=" * 70 , "\n"*3)

    while True:

        try:

            choice = int(input("What would you like to have : \n1.Starter. \n2.Main Course. \n3.Bread / Rice \n4.Dessert. \n5.Drinks. \n6.Generate Bill. \n7.Checkout. \n8.Remove item. \n9.Exit.\n\n"))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if(choice == 1):

            starter(order)
            print()

        elif(choice == 2):

            main_course(order)
            print()

        elif(choice == 3):

            bread_rice(order)
            print()

        elif(choice == 4):

            dessert(order)
            print()

        elif(choice == 5):

            Drinks(order)
            print()

        elif(choice == 6):

            if not order.items:

                print("Your cart is empty.")

            else:

                print("\n========== BILL ==========")
                order.show_orders()
                print()
             
        elif(choice == 7):

            order.checkout()
            print()

        elif(choice == 8):
            order.remove_item()
            print()

        elif(choice == 9):

            print("\nThank you for visiting!")
            break

        else:
            print("Wrong Choice")

main()