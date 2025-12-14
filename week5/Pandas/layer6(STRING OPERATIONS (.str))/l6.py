import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\sales_data_sample.csv", encoding="latin1")
#LOWER / UPPER / STRIP
df['COUNTRY'] = df['COUNTRY'].str.upper()
df['CITY'] = df['CITY'].str.strip()
print (df['CITY'])

# CONTAINS / STARTSWITH
df[df['CITY'].str.contains('York')]
df[df['CITY'].str.startswith('S')]
print (df[df['CITY'].str.startswith('S')])

# REPLACE TEXT
df['PRODUCTLINE'] = df['PRODUCTLINE'].str.replace('Cars', 'Vehicles')
print (df['PRODUCTLINE'])       