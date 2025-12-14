import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\sales_data_sample.csv", encoding="latin1")
print (df)
# BASIC GROUPBY USAGE
df.groupby('COUNTRY')['SALES'].sum()
print (df.groupby('COUNTRY')['SALES'].sum())
df.groupby('COUNTRY')['SALES'].sum()
print (df.groupby('COUNTRY')['SALES'].mean())

# MULTIPLE AGGREGATIONS
df.groupby('COUNTRY')['SALES'].agg(['sum', 'mean', 'max'])
print (df.groupby('COUNTRY')['SALES'].agg(['sum', 'mean', 'max']))

# SORTING GROUPED RESULTS
df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)
print (df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False))

# RESET INDEX
country_sales = df.groupby('COUNTRY')['SALES'].sum().reset_index()
print (country_sales)