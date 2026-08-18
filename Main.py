#initialize a class that has objects of FoodItems
class FoodItem:
    def __init__(self,name,category,type,price):
        self.name = name    #stores name of the food item example paneer tikka.
        self.category = category    #stores catagory of the food item example starter.
        self.type = type    #stores type of the food item example veg.
        self.price = price  #stores price of the food item example 250.

# Function that has all the starters.
def starter():
    choice2 = int(input("Enter :\n1.For veg items.\n2.For non veg items.\n"))   # takes out choice for veg or non veg, 1 for veg and 2 for non veg.
    if choice2 == 1:
        vitem1 = FoodItem("Paneer tikka","Starter","Veg",250)
        vitem2 = FoodItem("Crispy Chilli Baby Corn","Starter","Veg",200)
        vitem3 = FoodItem("Hara Bhara Kebab","Starter","Veg",160)
        vitem4 = FoodItem("Veg Manchurian","Starter","Veg",180)
        vitem5 = FoodItem("Chilli Mushroom","Starter","Veg",220)
        lv = [vitem1,vitem2,vitem3,vitem4,vitem5]   #list of veg items.
        for i in lv:    #prints veg items with their price
            print(i.name," - ",i.price)
    elif choice2 == 2:
        nvitem1 = FoodItem("Chicken tikka","Starter","Non Veg",300)
        nvitem2 = FoodItem("Chilli Chicken","Starter","Non Veg",260)
        nvitem3 = FoodItem("Fish Fingers","Starter","Non Veg",280)
        nvitem4 = FoodItem("Chicken 65","Starter","Non Veg",240)
        nvitem5 = FoodItem("Mutton Seekh Kebab","Starter","Non Veg",380)
        lnv = [nvitem1,nvitem2,nvitem3,nvitem4,nvitem5] # list of non veg items.
        for i in lnv:   #prints non veg items with their price
             print(i.name," - ",i.price)

# Function that has all the main courses.
def main_course():
    choice2 = int(input("Enter :\n1.For veg items.\n2.For non veg items.\n"))   # takes out choice for veg or non veg, 1 for veg and 2 for non veg.
    if choice2 == 1:
        vitem1 = FoodItem("Soya Chunks Masala","Main Course","Veg",180)
        vitem2 = FoodItem("Palak Paneer","Main Course","Veg",280)
        vitem3 = FoodItem("Kadai Paneer","Main Course","Veg",290)
        vitem4 = FoodItem("Dal Tadka","Main Course","Veg",180)
        vitem5 = FoodItem("Vegetable Jalfrezi","Main Course","Veg",240)
        lv = [vitem1,vitem2,vitem3,vitem4,vitem5]   #list of veg items.
        for i in lv:    #prints veg items with their price
            print(i.name," - ",i.price)
    elif choice2 == 2:
        nvitem1 = FoodItem("Grilled Chicken Breast","Main Course","Non Veg",400)
        nvitem2 = FoodItem("Chicken Tikka Masala","Main Course","Non Veg",350)
        nvitem3 = FoodItem("Macher Jhol (Bengali Fish Curry","Main Course","Non Veg",300)
        nvitem4 = FoodItem("Mutton Rogan Josh","Main Course","Non Veg",450)
        nvitem5 = FoodItem("Bhuna Gosht","Main Course","Non Veg",480)
        lnv = [nvitem1,nvitem2,nvitem3,nvitem4,nvitem5] # list of non veg items.
        for i in lnv:   #prints non veg items with their price
            print(i.name," - ",i.price)

# Function that has all the dessert.
def dessert():




print("=" * 100)
print("\t" * 6, "MENU")
print("=" * 100 , "\n"*3)
while(True):
    choice = int(input("What would tou like to have : \n 1.Starter. \n 2.Main Course. \n3.Bread / Rice \n 4.Dessert. \n 5.View cart. \n 6.Generate Bill. \n 7.exit"))
    if(choice == 1):
        starter()
    elif(choice == 2):
        main_course()
    elif(choice == 3):
        bread_rice()
    elif(choice == 4):
        dessert()
    elif(choice == 5):
        view_cart()
    elif(choice == 6):
        generate_bill()
    elif(choice == 7):
        break
    else:
        print("Wrong Choice")