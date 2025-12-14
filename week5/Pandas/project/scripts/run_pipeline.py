import pandas as pd
import os

# SET BASE PROJECT PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "..", "data", "sales_data_sample.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cleaned_sales.csv")

# LOAD DATA
df = pd.read_csv(DATA_PATH, encoding="latin1")
print("Data loaded:", df.shape)

# CLEANING
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

df['STATE'] = df['STATE'].fillna("Unknown")
df['POSTALCODE'] = df['POSTALCODE'].fillna("000000")
df['ADDRESSLINE2'] = df['ADDRESSLINE2'].fillna("_")
df['TERRITORY'] = df['TERRITORY'].fillna("Unknown")

df.drop_duplicates(inplace=True)

# FEATURE ENGINEERING

df['YEAR'] = df['ORDERDATE'].dt.year
df['MONTH'] = df['ORDERDATE'].dt.month
df['REVENUE'] = df['PRICEEACH'] * df['QUANTITYORDERED']


# FILTERING (LAYER 3 PRACTICAL USE)

df = df[df['STATUS'] == 'Shipped']
df = df[df['SALES'] > 1000]


# SAVE OUTPUT# 
os.makedirs(OUTPUT_DIR, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned data saved at:", OUTPUT_FILE)
