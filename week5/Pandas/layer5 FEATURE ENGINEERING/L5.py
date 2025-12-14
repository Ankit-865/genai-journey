import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\sales_data_sample.csv", encoding="latin1")
print (df)
# CREATE NEW COLUMNS
# Revenue (cross-check)
df['REVENUE'] = df['PRICEEACH'] * df['QUANTITYORDERED']
print (df[['PRICEEACH', 'QUANTITYORDERED', 'REVENUE']])
# High / Low Sales Flag
df['HIGH_SALES'] = df['SALES'] > 5000
print (df[['SALES', 'HIGH_SALES']])

# APPLY FUNCTION
# Add GST (18%)
df['SALES_WITH_GST'] = df['SALES'].apply(lambda x: x * 1.18)
print (df[['SALES', 'SALES_WITH_GST']])

# MAP FUNCTION
#  Encode DEALSIZE
df['DEALSIZE_CODE'] = df['DEALSIZE'].map({
    'Small': 1,
    'Medium': 2,
    'Large': 3
})
print (df[['DEALSIZE', 'DEALSIZE_CODE']])

# DATE FEATURES
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month
df['DAY'] = df['ORDERDATE'].dt.day
df['QUARTER'] = df['ORDERDATE'].dt.quarter
print (df[['ORDERDATE', 'YEAR', 'MONTH', 'DAY', 'QUARTER']])
