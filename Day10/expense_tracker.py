# Day 10: Class-Based Expense Tracker with File Handling  
class ExpenseManager:  
        def __init__(self, filename="expenses.csv"):  
            self.filename = filename  
            self.expenses = []  
            self.load_expenses()  # Load data on init  

        def save_expenses(self):  
            try:  
                with open(self.filename, "w") as f:  # Overwrite mode for now  
                    for expense in self.expenses:  
                        f.write(f"{expense['name']},{expense['category']},{expense['amount']}\n")  
            except IOError:  
                print(" Error saving expenses!")  

        def load_expenses(self):  
            try:  
                with open(self.filename, "r") as f:  
                    for line in f:  
                        name, category, amount = line.strip().split(",")  
                        self.expenses.append({"name": name, "category": category, "amount": float(amount)})  
            except FileNotFoundError:  
                pass  # Start empty if file not found  

        def add_expense(self, name, category, amount):  
            if not name or amount < 0:  
                print(" Invalid input! Name required and amount must be positive.")  
                return  
            self.expenses.append({"name": name, "category": category, "amount": amount})  
            self.save_expenses()  
            print("✅ Expense added!")  

        def view_expenses(self):  
            if not self.expenses:  
                print("📭 No expenses recorded.")  
                return  
            total = 0  
            for expense in self.expenses:  
                print(f"{expense['name']} ({expense['category']}): ₹{expense['amount']}")  
                total += expense['amount']  
            print(f" Total: ₹{total}")  

    # Main CLI Loop  
manager = ExpenseManager()  
while True:  
        print("\n💸 Expense Tracker")  
        print("1. Add Expense")  
        print("2. View Expenses")  
        print("3. Exit")  
        choice = input("Choose an option: ")  
        if choice == "1":  
            name = input("Enter expense name: ")  
            category = input("Enter category (e.g., Food/Travel): ")  
            try:  
                amount = float(input("Enter amount: "))  
                manager.add_expense(name, category, amount)  
            except ValueError:  
                print(" Enter a valid number!")  
        elif choice == "2":  
            manager.view_expenses()  
        elif choice == "3":  
            print(" Goodbye!")  
            break  
        else:  
            print(" Invalid choice. Try again.")