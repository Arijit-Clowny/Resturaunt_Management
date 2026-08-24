
from models import *

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
