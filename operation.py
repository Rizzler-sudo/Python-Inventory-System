import datetime
from write import write_products

# Function to sell products
def sell_product(products):
    sold_items = []
    total_amount = 0
    
    customer_name = input("Enter customer name: ")
    while customer_name == "":
        customer_name = input("Name cannot be empty: ")
    customer_phone = input("Enter customer number: ")
    while not customer_phone.isdigit():
        customer_phone = input("Enter a valid phone number: ")
    while True:
        print("\nAvailable Products:")
        print("ID  Name         Brand          Rate     Stock    Country")
        print("----------------------------------------------------------")
        for i in range(len(products)):
            p = products[i]
            print(str(i + 1) + "  " + p["Name"] + " " * (14 - len(p["Name"])) +
                  p["Brand"] + " " * (15 - len(p["Brand"])) +
                  "Rs" + str(p["Rate"]) + " " * (8 - len(str(p["Rate"]))) +
                  str(p["Stock"]) + " " * (9 - len(str(p["Stock"]))) +
                  p["Country"])

        print("\nDear customer, we are having buy 3 Get 1 Offer!")

        try:
            product_id = int(input("\nEnter product ID to sell: ")) - 1
            if product_id < 0 or product_id >= len(products):
                print("Invalid product ID.")
                continue
        except:
            print("Please enter a valid number.")
            continue

        selected_product = products[product_id]
        available = selected_product["Stock"]

        try:
            quantity = int(input("Enter quantity to purchase (Available: " + str(available) + "): "))
        except:
            print("Invalid quantity.")
            continue
        
        #offer logic: Buy 3 Get 1 Free
        free_items = quantity // 3
        total_deduct = quantity + free_items

        if quantity <= 0 or total_deduct > available:
            print("Sorry,Not enough stock available.")
            continue

        if free_items > 0:
            print("Congratulations", customer_name + " you have recevied", free_items, "free items on our Buy 3 Get 1 Free offer." ) 

        selected_product["Stock"] = selected_product["Stock"] - total_deduct
        cost = selected_product["Rate"] * quantity
        total_amount = total_amount + cost

        sold_items.append([selected_product["Name"], quantity, free_items, cost])

        more = input(" Do you want to purchase more? (y/n): ").lower()
        if more != 'y':
            break

    write_products(products)
    print("Bill generated for", customer_name + ".")

    # Invoice
    invoice = "\n------------------------------------------------------------\n"
    invoice += "            WeCare - Sales Invoice                    \n"
    invoice += "------------------------------------------------------------\n"
    invoice += "Customer Name : " + customer_name + "\n"
    invoice += "Phone Number  : " + customer_phone + "\n"
    invoice += "Date          : " + str(datetime.datetime.now()) + "\n"
    invoice += "------------------------------------------------------------\n"
    invoice += "Product     Qty    Free    Price\n"

    for item in sold_items:
        name = item[0]
        qty = str(item[1])
        free = str(item[2])
        price = str(item[3])
        invoice += name + " " * (13 - len(name)) + qty + " " * (6 - len(qty)) + free + " " * (7 - len(free)) + price + "\n"

    invoice += "------------------------------------------------------------\n"
    invoice += "Total Amount: Rs " + str(total_amount) + "\n"
    invoice += "Thank you for shopping with us,!\n"
    invoice += "------------------------------------------------------------\n"

    print(invoice)

    try:
        f = open("invoice_sell.txt", "w")
        f.write(invoice)
        f.close()
    except:
        print("Error saving invoice")


# Function to restock products
def restock_product(products):
    restocked_items = []

    supplier_name = input("Enter supplier name: ")
    while supplier_name == "":
        supplier_name = input("Name cannot be empty: ")

    supplier_phone = input("Enter phone number: ")
    while not supplier_phone.isdigit():
        supplier_phone = input("Enter a valid phone number: ")

    while True:
        print("\nAvailable Products at our WeCare WholeSale:")
        print("ID  Name         Brand          Rate     Stock     Country")
        print("-------------------------------------------------------------")
        for i in range(len(products)):
            p = products[i]
            print(str(i + 1) + "  " + p["Name"] + " " * (14 - len(p["Name"])) +
                  p["Brand"] + " " * (15 - len(p["Brand"])) +
                  "Rs" + str(p["Rate"]) + " " * (8 - len(str(p["Rate"]))) +
                  str(p["Stock"]) + " " * (9 - len(str(p["Stock"]))) +
                  p["Country"])
        try:
            product_id = int(input("\nEnter product ID to restock: ")) - 1
            if product_id < 0 or product_id >= len(products):
                print("Invalid product ID.")
                continue
        except:
            print("Enter valid number.")
            continue

        try:
            add_qty = int(input("Enter quantity to add: "))
            if add_qty <= 0:
                print("Quantity must be more than zero.")
                continue
        except:
            print("Invalid input.")
            continue

        products[product_id]["Stock"] = products[product_id]["Stock"] + add_qty
        restocked_items.append([products[product_id]["Name"], add_qty])

        more = input(" Do you want to restock more? (y/n): ").lower()
        if more != 'y':
            break

    write_products(products)

    # Invoice
    invoice = "\n--------------------------------------------------\n"
    invoice += "           WeCare - Restock Invoice              \n"
    invoice += "--------------------------------------------------\n"
    invoice += "Supplier Name : " + supplier_name + "\n"
    invoice += "Phone Number  : " + supplier_phone + "\n"
    invoice += "Date          : " + str(datetime.datetime.now()) + "\n"
    invoice += "--------------------------------------------------\n"
    invoice += "Product       Quantity Added\n"

    for item in restocked_items:
        name = item[0]
        qty = str(item[1])
        invoice += name + " " * (14 - len(name)) + qty + "\n"

    invoice += "--------------------------------------------------\n"
    invoice += "Restock Completed Successfully.\n"
    invoice += "--------------------------------------------------\n"

    print(invoice)

    try:
        f = open("invoice_restock.txt", "w")
        f.write(invoice)
        f.close()
    except:
        print("Error saving invoice_stock.txt file")
