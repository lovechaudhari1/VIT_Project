class SimpleInventory:
    def __init__(self):
        self.items = {}

    def add_item(self, code, name, quantity, price):
        if code not in self.items:
            self.items[code] = {"name": name, "quantity": quantity, "price": price}
            print(f"Added {name} with code {code}.")
        else:
            print("Item code already exists.")

    def update_stock(self, code, quantity):
        if code in self.items:
            self.items[code]["quantity"] += quantity
            print(f"Updated stock for {self.items[code]['name']} to {self.items[code]['quantity']}.")
        else:
            print("Item not found.")

    def view_item(self, code):
        if code in self.items:
            item = self.items[code]
            print(f"Code: {code}\nName: {item['name']}\nQuantity: {item['quantity']}\nPrice: ${item['price']}")
        else:
            print("Item not found.")

    def list_all(self):
        print("Inventory List:")
        for code, info in self.items.items():
            print(f"{code}: {info['name']} - Qty: {info['quantity']} - Price: ${info['price']}")

def main():
    inv = SimpleInventory()
    while True:
        print("\n1. Add Item\n2. Update Stock\n3. View Item\n4. List Inventory\n5. Exit")
        choice = input("Choice: ")

        if choice == "1":
            c = input("Enter item code: ")
            n = input("Enter item name: ")
            q = int(input("Enter quantity: "))
            p = float(input("Enter price: "))
            inv.add_item(c, n, q, p)
        elif choice == "2":
            c = input("Enter item code: ")
            q = int(input("Enter quantity to add or remove (use negative to remove): "))
            inv.update_stock(c, q)
        elif choice == "3":
            c = input("Enter item code: ")
            inv.view_item(c)
        elif choice == "4":
            inv.list_all()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
