import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\Pandas\sales_data_sample.csv", encoding="latin1")
# coloumn selection 
df.nlargest(10, 'SALES')
print (df)
df[df['PRODUCTLINE'] == 'Classic Cars']
print (df)
df[df['SALES'] > 50000]
print (df)