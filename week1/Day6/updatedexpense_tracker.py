# Day 6: Enhanced Expense Tracker with File Handling
def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, "w") as f:
        for expense in expenses:
            f.write(f"{expense['name']},{expense['amount']}\n")

def load_expenses(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, "r") as f:
            for line in f:
                name, amount = line.strip().split(",")
                expenses.append({"name": name, "amount": float(amount)})
    except FileNotFoundError:
        pass  # Ignore if file doesn't exist yet
    return expenses

def add_expense(expenses):
    name = input("Enter expense name (e.g., food): ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount >= 0:
                break
            print(" Amount cannot be negative!")
        except ValueError:
            print(" Enter a valid number!")
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print(" Expense added!")

def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses recorded.")
        return
    total = 0
    for expense in expenses:
        print(f"{expense['name']}: ₹{expense['amount']}")
        total += expense['amount']
    print(f" Total: ₹{total}")

def find_highest_expense(expenses):
    if not expenses:
        print("📭 No expenses to check.")
        return
    highest = expenses[0]
    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense
    print(f"🔝 Highest Expense: {highest['name']} - ₹{highest['amount']}")

# Main CLI Loop
expenses = load_expenses()
while True:
    print("\n💸 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Highest Expense")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        find_highest_expense(expenses)
    elif choice == "4":
        save_expenses(expenses)  # Save before exit
        print("👋 Goodbye!")
        break
    else:
        print(" Invalid choice. Try again.")