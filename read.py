# read.py – Reads data from products.txt and shows header info
def get_products():
    products = []
    try:
        with open("products.txt", "r") as file:
            for line in file:
                if line != "\n":
                    parts = line.split(",")
                    if len(parts) == 5:  # Only process lines with 5 parts
                        name = parts[0]
                        brand = parts[1]
                        rate = float(parts[2])
                        stock = int(float(parts[3]))  # handles '400.0' type input
                        country = parts[4].replace("\n", "")
                        product = {
                            "Name": name,
                            "Brand": brand,
                            "Rate": rate,
                            "Stock": stock,
                            "Country": country
                        }
                        products.append(product)
    except FileNotFoundError:
        print("Error: products.txt file not found.")
    return products


def header():
    print("------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\tWecare Product WholeSale")
    print("\t\t\tJhamsikhel, Lalitpur | Contact No: 9824219410")
    print("\t\t\t\tWe provide best skincare items.")
    print("------------------------------------------------------------------------")
    print("Welcome to the system admin, Sir.")
