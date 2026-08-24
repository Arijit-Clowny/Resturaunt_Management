from models import *
from order_utils import *

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

            vitem1 = FoodItem(1,"Paneer tikka",250)
            vitem2 = FoodItem(2,"Crispy Chilli Baby Corn",200)
            vitem3 = FoodItem(3,"Hara Bhara Kebab",160)
            vitem4 = FoodItem(4,"Veg Manchurian",180)
            vitem5 = FoodItem(5,"Chilli Mushroom",220)

            # Initialize all veg starters in a list.

            lv = [vitem1,vitem2,vitem3,vitem4,vitem5]

            print("\n----------- VEG STARTERS -----------")

            for i in lv:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("------------------------------------\n")

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

            print("\n--------- NON-VEG STARTERS ---------")

            for i in lnv:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("------------------------------------\n")

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

            print("\n--------- VEG MAIN COURSES ---------")

            for i in lv:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("------------------------------------\n")

            take_order(lv , order)

        elif choice2 == 2:

            nvitem1 = FoodItem(1,"Grilled Chicken Breast",400)
            nvitem2 = FoodItem(2,"Chicken Tikka Masala",350)
            nvitem3 = FoodItem(3,"Macher Jhol (Fish Curry)",300)
            nvitem4 = FoodItem(4,"Mutton Rogan Josh",450)
            nvitem5 = FoodItem(5,"Bhuna Gosht",480)

            # Initialize all non veg Main courses in a list.

            lnv = [nvitem1,nvitem2,nvitem3,nvitem4,nvitem5]

            print("\n------ NON-VEG MAIN COURSES -------")
            
            for i in lnv:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("-----------------------------------\n")
            
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
            item3 = FoodItem(3,"Gulab jamun and ice cream",160)
            item4 = FoodItem(4,"Blueberry cheesecake",140)
            item5 = FoodItem(5,"Rabdi jalebi",120)
    
            # Initialize all desserte in a list.
    
            l = [item1,item2,item3,item4,item5]

            print("\n------------- DESSERTS -------------")
    
            for i in l:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("------------------------------------\n")

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

            print("\n----------- BREAD / RICE -----------")
        
            for i in l:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("------------------------------------\n")

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

            print("\n-------------- DRINKS --------------")
        
            for i in l:
                print(f"{i.index}.{i.name:<25} - ₹ {i.price}")

            print("------------------------------------\n")

            take_order(l , order)

        elif choice2 == 2:
                        
            return
                
        else:
                
            print("Wrong choice.\n")
