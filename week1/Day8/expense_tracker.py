# Day 8: Enhanced Expense Tracker with Category Reporting  

def save_expenses(expenses, filename="expenses.csv"):  
        with open(filename, "a") as f:  # Append mode  
            for expense in expenses:  
                f.write(f"{expense['name']},{expense['category']},{expense['amount']}\n")  

def load_expenses(filename="expenses.csv"):  
        expenses = []  
        try:  
            with open(filename, "r") as f:  
                for line in f:  
                    name, category, amount = line.strip().split(",")  
                    expenses.append({"name": name, "category": category, "amount": float(amount)})  
        except FileNotFoundError:  
            pass  # Ignore if file doesn't exist yet  
        return expenses  

def add_expense(expenses):  
        name = input("Enter expense name (e.g., food): ")  
        category = input("Enter category (e.g., Food/Travel): ")  
        while True:  
            try:  
                amount = float(input("Enter amount: "))  
                if amount >= 0:  
                    break  
                print(" Amount cannot be negative!")  
            except ValueError:  
                print(" Enter a valid number!")  
        expenses.append({"name": name, "category": category, "amount": amount})  
        save_expenses([expenses[-1]])  # Save only the new expense  
        print("✅ Expense added!")  

def view_expenses(expenses):  
        if not expenses:  
            print(" No expenses recorded.")  
            return  
        total = 0  
        for expense in expenses:  
            print(f"{expense['name']} ({expense['category']}): ₹{expense['amount']}")  
            total += expense['amount']  
        print(f" Total: ₹{total}")  

def find_highest_expense(expenses):  
        if not expenses:  
            print(" No expenses to check.")  
            return  
        highest = expenses[0]  
        for expense in expenses:  
            if expense["amount"] > highest["amount"]:  
                highest = expense  
        print(f" Highest Expense: {highest['name']} ({highest['category']}) - ₹{highest['amount']}")  

def view_category_report(filename="expenses.csv"):  
        totals = {}  
        try:  
            with open(filename, "r") as f:  
                for line in f:  
                    name, category, amount = line.strip().split(",")  
                    totals[category] = totals.get(category, 0) + float(amount)  
            for category, total in totals.items():  
                print(f" {category}: ₹{total}")  
        except FileNotFoundError:  
            print("📭 No data file found.")  

    # Main CLI Loop  
expenses = load_expenses()  
while True:  
        print("\n💸 Expense Tracker")  
        print("1. Add Expense")  
        print("2. View Expenses")  
        print("3. Highest Expense")  
        print("4. View Category Report")  
        print("5. Exit")  
        choice = input("Choose an option: ")  
        if choice == "1":  
            add_expense(expenses)  
        elif choice == "2":  
            view_expenses(expenses)  
        elif choice == "3":  
            find_highest_expense(expenses)  
        elif choice == "4":  
            view_category_report()  
        elif choice == "5":  
            print("👋 Goodbye!")  
            break  
        else:  
            print(" Invalid choice. Try again.")