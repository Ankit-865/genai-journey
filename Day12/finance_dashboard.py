# Day 12: Personal Finance Dashboard
class FinanceManager:
    def __init__(self, filename="finance_data.csv"):
        self.filename = filename
        self.transactions = []
        self.load_data()

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                for trans in self.transactions:
                    f.write(f"{trans['name']},{trans['amount']},{trans['type']}\n")
        except IOError:
            print("⚠️ Error saving data!")

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    name, amount, trans_type = line.strip().split(",")
                    self.transactions.append({"name": name, "amount": float(amount), "type": trans_type})
        except FileNotFoundError:
            pass

    def add_transaction(self, name, amount, trans_type):
        if not name or amount < 0:
            print("⚠️ Invalid input! Name required and amount must be positive.")
            return
        self.transactions.append({"name": name, "amount": amount, "type": trans_type})
        self.save_data()
        print("✅ Transaction added!")

    def view_summary(self):
        if not self.transactions:
            print("📭 No transactions recorded.")
            return
        income = sum(t["amount"] for t in self.transactions if t["type"] == "income")
        expense = sum(t["amount"] for t in self.transactions if t["type"] == "expense")
        balance = income - expense
        print(f"💰 Income: ₹{income}")
        print(f"💸 Expense: ₹{expense}")
        print(f"💵 Balance: ₹{balance}")

# Main CLI Loop
manager = FinanceManager()
while True:
    print("\n💼 Personal Finance Dashboard")
    print("1. Add Transaction")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter transaction name: ")
        try:
            amount = float(input("Enter amount: "))
            trans_type = input("Enter type (income/expense): ").lower()
            if trans_type not in ["income", "expense"]:
                print("⚠️ Type must be 'income' or 'expense'!")
                continue
            manager.add_transaction(name, amount, trans_type)
        except ValueError:
            print("⚠️ Enter a valid number!")
    elif choice == "2":
        manager.view_summary()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again!")