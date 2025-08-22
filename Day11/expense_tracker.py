# Day 11: OOP Inheritance and Reporting in Expense Tracker  
class ExpenseManager:  
        def __init__(self, filename="expenses.csv"):  
            self.filename = filename  
            self.expenses = []  
            self.load_expenses()  

        def save_expenses(self):  
            try:  
                with open(self.filename, "w") as f:  
                    for expense in self.expenses:  
                        f.write(f"{expense['name']},{expense['category']},{expense['amount']}\n")  
            except IOError:  
                print("⚠️ Error saving expenses!")  

        def load_expenses(self):  
            try:  
                with open(self.filename, "r") as f:  
                    for line in f:  
                        name, category, amount = line.strip().split(",")  
                        self.expenses.append({"name": name, "category": category, "amount": float(amount)})  
            except FileNotFoundError:  
                pass  

        def add_expense(self, name, category, amount):  
            if not name or amount < 0:  
                print("⚠️ Invalid input! Name required and amount must be positive.")  
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
            print(f"💰 Total: ₹{total}")  

class ReportManager(ExpenseManager):  
        def generate_report(self):  
            totals = {}  
            try:  
                with open(self.filename, "r") as f:  
                    for line in f:  
                        name, category, amount = line.strip().split(",")  
                        totals[category] = totals.get(category, 0) + float(amount)  
                for category, total in totals.items():  
                    print(f"🏷️ {category}: ₹{total}")  
            except FileNotFoundError:  
                print("📭 No data file found.")  

    # Main CLI Loop  
manager = ReportManager()  
while True:  
        print("\n💸 Expense Tracker")  
        print("1. Add Expense")  
        print("2. View Expenses")  
        print("3. Generate Report")  
        print("4. Exit")  
        choice = input("Choose an option: ")  
        if choice == "1":  
            name = input("Enter expense name: ")  
            category = input("Enter category (e.g., Food/Travel): ")  
            try:  
                amount = float(input("Enter amount: "))  
                manager.add_expense(name, category, amount)  
            except ValueError:  
                print("⚠️ Enter a valid number!")  
        elif choice == "2":  
            manager.view_expenses()  
        elif choice == "3":  
            manager.generate_report()  
        elif choice == "4":  
            print("👋 Goodbye!")  
            break  
        else:  
            print("❌ Invalid choice. Try again.")