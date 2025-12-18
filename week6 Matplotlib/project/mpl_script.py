
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build full path to CSV file
CSV_PATH = os.path.join(BASE_DIR, "sales_data.csv")

# Read the CSV file
df = pd.read_csv(CSV_PATH, encoding="latin1")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

# VISUALIZATION 1: SALES DISTRIBUTION
plt.figure(figsize=(8, 5))
plt.hist(df["SALES"], bins=30)
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.title("Distribution of Sales")
plt.tight_layout()
plt.show()


# VISUALIZATION 2: SALES BY PRODUCT LINE

sales_by_product = df.groupby("PRODUCTLINE")["SALES"].sum()

plt.figure(figsize=(10, 6))
plt.bar(sales_by_product.index, sales_by_product.values)
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product Line")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. VISUALIZATION 3: MONTHLY SALES TREND
monthly_sales = df.groupby("MONTH_ID")["SALES"].sum()

plt.figure(figsize=(8, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.show()
