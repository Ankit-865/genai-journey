import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\sales_data_sample.csv", encoding="latin1")

# Check duplicates
df.duplicated().sum()
print (df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)
print (df)
