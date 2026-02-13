# main.py - Entry p1oint of the program

from read import get_products, header
from operation import sell_product, restock_product

def main():
    header()

    # Read products from file at the start
    products = get_products()

    # Show the main menu
    while True:
        print("\nMain Menu:")
        print("1. Sell Products")
        print("2. Restock Products")
        print("0. Exit")

        choice = input("Enter your choice (0-2): ")

        if choice == "1":
            sell_product(products)
        elif choice == "2":
            restock_product(products)
        elif choice == "0":
            print("Thank you for using WeCare Product Wholesale System. Have a good day, Sir!")
            break
        #Handling the wrong input
        else:
            print("Invalid Input." "Your choice", choice, "doesn't match our requirements.Please try again")

# Call the main function
main()

