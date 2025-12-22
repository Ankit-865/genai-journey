import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
df = pd.read_csv("C:\\genai-journey\\week7.seaborn\\project\\sales_data.csv", encoding="latin1")

print(df.head())
print(df.info())

# visualization1

plt.figure(figsize=(8,5))
sns.histplot(df["SALES"], bins=30, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()

# visualization2
plt.figure(figsize=(10,6))
sns.barplot(
    x="PRODUCTLINE",
    y="SALES",
    data=df,
    estimator=sum
)
plt.xticks(rotation=45)
plt.title("Total Sales by Product Line")
plt.show()

# Visualization3
plt.figure(figsize=(8,5))
sns.boxplot(
    x="DEALSIZE",
    y="SALES",
    data=df
)
plt.title("Sales Distribution by Deal Size")
plt.show()

# visualization4
monthly_sales = df.groupby("MONTH_ID")["SALES"].sum().reset_index()

plt.figure(figsize=(8,5))
sns.lineplot(
    x="MONTH_ID",
    y="SALES",
    data=monthly_sales,
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# visualization5
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="QUANTITYORDERED",
    y="SALES",
    data=df,
    hue="DEALSIZE"
)
plt.title("Quantity Ordered vs Sales")
plt.show()

# visualization6
numeric_df = df.select_dtypes("number")
corr = numeric_df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
