# write.py

# Function to write updated product data back to products.txt
def write_products(products):
    try:
        with open("products.txt", "w") as file:
            for p in products:
                line = p["Name"] + "," + p["Brand"] + "," + str(p["Rate"]) + "," + str(p["Stock"]) + "," + p["Country"] + "\n"
                file.write(line)
    except:
        print("Error saving products.txt file.")
