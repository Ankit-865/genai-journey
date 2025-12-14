import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\sales_data_sample.csv", encoding="latin1")
print (df)
# SORT VALUES
df.sort_values(by='SALES', ascending=False)
print (df.sort_values(by='SALES', ascending=False))

# Sort by multiple columns
df.sort_values(by=['COUNTRY', 'SALES'], ascending=[True, False])
print (df.sort_values(by=['COUNTRY', 'SALES'], ascending=[True, False]))

# TOP / BOTTOM RECORDS
# Top 10 highest sales orders
df.nlargest(10, 'SALES')
print (df.nlargest(10, 'SALES'))
# Bottom 10 lowest sales orders
df.nsmallest(10, 'SALES')
print (df.nsmallest(10, 'SALES'))
# RANKING
# Rank orders by sales
df['SALES_RANK'] = df['SALES'].rank(ascending=False)
print (df[['ORDERNUMBER', 'SALES', 'SALES_RANK']])