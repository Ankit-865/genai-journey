import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\sales_data_sample.csv", encoding="latin1")
# CHECK NULLS
df.isnull().sum()
print (df.isnull().sum())

# FILL NULLS
df['STATE'] = df['STATE'].fillna('Unknown')
df['POSTALCODE'] = df['POSTALCODE'].fillna('000000')
print (df[['STATE', 'POSTALCODE']])

# DROP NULLS
df.dropna(subset=['SALES'], inplace=True)
print (df[['ORDERNUMBER', 'SALES']])