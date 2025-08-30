# day7_csv_test.py
data = [{"name": "food", "amount": 500}, {"name": "travel", "amount": 300}]
with open("test.csv", "w") as f:
    for item in data:
        f.write(f"{item['name']},{item['amount']}\n")