#category_sum.py
def sum_by_category(filename="test.csv"):
    totals = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, category, amount = line.strip().split(",")
                totals[category] = totals.get(category, 0) + float(amount)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Creating an empty file...")
        with open(filename, "w") as f:
            pass  # Creates empty file
    return totals

# Test the function and print result
result = sum_by_category()
if result:
    print("Category Totals:", result)
else:
    print("No data to summarize. Add some data to test.csv!")