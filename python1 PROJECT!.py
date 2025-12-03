# inventory_management.py

# List to store inventory items
inventory = []


# Function to add a new item
def add_item():
    print("\n=== Add Item ===")
    name = input("Enter item name: ").strip()

    # Validate price input
    while True:
        try:
            price = float(input("Enter item price: "))
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number for price.")

    # Validate quantity input
    while True:
        try:
            quantity = int(input("Enter item quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid integer for quantity.")

    category = input("Enter item category: ").strip()

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"{name} has been added to the inventory.")


# Function to update an existing item
def update_item():
    print("\n=== Update Item ===")
    name = input("Enter the name of the item to update: ").strip()
    for item in inventory:
        if item["name"].lower() == name.lower():
            # Update price
            while True:
                try:
                    item["price"] = float(input("Enter new price: "))
                    if item["price"] < 0:
                        print("Price cannot be negative. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Enter a valid number for price.")

            # Update quantity
            while True:
                try:
                    item["quantity"] = int(input("Enter new quantity: "))
                    if item["quantity"] < 0:
                        print("Quantity cannot be negative. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Enter a valid integer for quantity.")

            # Update category
            item["category"] = input("Enter new category: ").strip()
            print(f"{name} has been updated.")
            return
    print(f"{name} not found in inventory.")


# Function to view all inventory items
def view_inventory():
    print("\n=== View Inventory ===")
    if not inventory:
        print("Inventory is empty.")
        return
    for idx, item in enumerate(inventory, start=1):
        print(
            f"{idx}. Name: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")


# Function to remove an item
def remove_item():
    print("\n=== Remove Item ===")
    name = input("Enter the name of the item to remove: ").strip()
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"{name} has been removed from inventory.")
            return
    print(f"{name} not found in inventory.")


# Function to search items by category
def search_by_category():
    print("\n=== Search by Category ===")
    category = input("Enter the category to search: ").strip()
    found_items = [item for item in inventory if item["category"].lower() == category.lower()]

    if not found_items:
        print(f"No items found in category '{category}'.")
        return

    print(f"Items in category '{category}':")
    for idx, item in enumerate(found_items, start=1):
        print(f"{idx}. Name: {item['name']}, Price: ${item['price']}, Quantity: {item['quantity']}")


# Main loop
def main():
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()