# Day 5: Personal Expense Tracker
def add_expense(expenses):
    name = input("Enter expense name (e.g., food): ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount >= 0:
                break
            print("⚠️ Amount cannot be negative!")
        except ValueError:
            print("⚠️ Enter a valid number!")
    expenses.append({"name": name, "amount": amount})
    print("✅ Expense added!")

def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses recorded.")
        return
    total = 0
    for expense in expenses:
        print(f"{expense['name']}: ₹{expense['amount']}")
        total += expense['amount']
    print(f"💰 Total: ₹{total}")

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
expenses = []
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
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")