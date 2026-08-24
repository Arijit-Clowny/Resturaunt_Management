from models import *
from menu import *
from order_utils import *


#------------------------------------------------------
# Main Function.
#------------------------------------------------------
    
def main():

    # One order object for the entire program.
    order = Order()

    print("=" * 60)
    print("\t" * 3, "MENU")
    print("=" * 60 , "\n"*3)

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

                print("\n================== BILL ==================")
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

if __name__ == "__main__":
    m = main()
    print(m)