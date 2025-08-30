# Day 9: Class-Based Expense Tracker  
class ExpenseManager:  
        def __init__(self):  
            self.expenses = []  
        def add_expense(self, name, category, amount):  
            if not name or amount < 0:  
                print("⚠️ Invalid input! Name required and amount must be positive.")  
                return  
            self.expenses.append({"name": name, "category": category, "amount": amount})  
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
                print("⚠️ Enter a valid number!")  
        elif choice == "2":  
            manager.view_expenses()  
        elif choice == "3":  
            print("👋 Goodbye!")  
            break  
        else:  
            print("❌ Invalid choice. Try again.")