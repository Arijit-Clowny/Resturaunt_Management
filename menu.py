from models import *
from order_utils import *
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

#------------------------------------------------------
# Starters.
#------------------------------------------------------

def starter(order):

    run = True

    while(run):

        try:

            choice2 = int(input("\nEnter :\n1.For Veg items.\n2.For Non-Veg.\n3.Go back.\n\n"))

        except ValueError:

            print("Please enter a valid number.\n")
            continue

        if choice2 == 1:

            items = get_food_objects("Starter","Veg")

            print("\n------------ VEG STARTERS ------------")

            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("--------------------------------------\n")

            # Takes order.

            take_order(items , order)
    
        elif choice2 == 2:

            items = get_food_objects("Starter","Non-Veg")

            print("\n--------- NON-VEG STARTERS ---------")

            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("------------------------------------\n")

            # Takes order.

            take_order(items , order)

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

            items = get_food_objects("Main Course","Veg")

            print("\n--------- VEG MAIN COURSES ---------")

            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("------------------------------------\n")

            take_order(items , order)

        elif choice2 == 2:

            items = get_food_objects("Main Course","Non-Veg")

            print("\n------ NON-VEG MAIN COURSES -------")
            
            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("-----------------------------------\n")
            
            take_order(items , order)

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

            items = get_food_objects("Dessert")
            

            print("\n------------- DESSERTS -------------")
    
            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("------------------------------------\n")

            take_order(items , order)

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

            items = get_food_objects("Bread/Rice")            

            print("\n----------- BREAD / RICE -----------")
        
            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("------------------------------------\n")

            take_order(items , order)

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

            items = get_food_objects("Drinks")

            print("\n-------------- DRINKS --------------")
        
            for item in items:
                print(f"{item.index}.{item.name:<25} - ₹ {item.price}")

            print("------------------------------------\n")

            take_order(items , order)

        elif choice2 == 2:
                        
            return
                
        else:
                
            print("Wrong choice.\n")
