# Day 13: Inventory Management System  
class InventoryManager:  
        def __init__(self, filename="inventory.csv"):  
            self.filename = filename  
            self.inventory = {}  
            self.load_inventory()  

        def save_inventory(self):  
            try:  
                with open(self.filename, "w") as f:  
                    for item, qty in self.inventory.items():  
                        f.write(f"{item},{qty}\n")  
            except IOError:  
                print("⚠️ Error saving inventory!")  

        def load_inventory(self):  
            try:  
                with open(self.filename, "r") as f:  
                    for line in f:  
                        item, qty = line.strip().split(",")  
                        self.inventory[item] = int(qty)  
            except FileNotFoundError:  
                pass  

        def add_item(self, item, quantity):  
            if not item or quantity < 0:  
                print("⚠️ Invalid input! Item name required and quantity must be positive.")  
                return  
            self.inventory[item] = self.inventory.get(item, 0) + quantity  
            self.save_inventory()  
            print(f"✅ Added {quantity} {item}(s) to inventory!")  

        def check_stock(self):  
            if not self.inventory:  
                print("📭 Inventory is empty.")  
                return  
            for item, qty in self.inventory.items():  
                print(f"📦 {item}: {qty} units")  

    # Main CLI Loop  
manager = InventoryManager()  
while True:  
        print("\n📦 Inventory Management")  
        print("1. Add Item")  
        print("2. Check Stock")  
        print("3. Exit")  
        choice = input("Choose an option: ")  
        if choice == "1":  
            item = input("Enter item name: ")  
            try:  
                qty = int(input("Enter quantity: "))  
                manager.add_item(item, qty)  
            except ValueError:  
                print("⚠️ Enter a valid number!")  
        elif choice == "2":  
            manager.check_stock()  
        elif choice == "3":  
            print("👋 Goodbye!")  
            break  
        else:  
            print("❌ Invalid choice. Try again!")