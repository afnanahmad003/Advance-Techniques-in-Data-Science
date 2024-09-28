# Sample product data
products = {
    1: {"pid": "P001", "name": "Product 1", "image": "image1.jpg", "rating": 4.5},
    2: {"pid": "P002", "name": "Product 2", "image": "image2.jpg", "rating": 3.8},
    3: {"pid": "P003", "name": "Product 3", "image": "image3.jpg", "rating": 4.9}
}

def show_products():
    print("\nShowing all products:")
    for key, product in products.items():
        print(f"ID: {key}, PID: {product['pid']}, Name: {product['name']}, Image: {product['image']}, Rating: {product['rating']}")
    print()

def add_product():
    new_id = max(products.keys()) + 1
    pid = input("Enter product ID (pid): ")
    name = input("Enter product name: ")
    image = input("Enter image name (e.g. image.jpg): ")
    rating = float(input("Enter product rating: "))
    products[new_id] = {"pid": pid, "name": name, "image": image, "rating": rating}
    print("Product added successfully!\n")

def delete_product():
    product_id = int(input("Enter the product ID to delete: "))
    if product_id in products:
        del products[product_id]
        print(f"Product ID {product_id} deleted successfully!\n")
    else:
        print("Product ID not found!\n")

def update_product_rating():
    product_id = int(input("Enter the product ID to update the rating: "))
    if product_id in products:
        new_rating = float(input("Enter new rating: "))
        products[product_id]["rating"] = new_rating
        print(f"Product ID {product_id} rating updated successfully!\n")
    else:
        print("Product ID not found!\n")

def main():
    while True:
        print("1. Show all Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        
        option = int(input("Enter option to continue: "))
        
        if option == 1:
            show_products()
        elif option == 2:
            add_product()
        elif option == 3:
            delete_product()
        elif option == 4:
            update_product_rating()
        elif option == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid option! Please try again.\n")

if __name__ == "__main__":
    main()