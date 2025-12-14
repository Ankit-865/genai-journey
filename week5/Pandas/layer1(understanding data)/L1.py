# head() , tail()
import pandas as pd
df= pd.read_csv("C:\genai-journey\week5\Pandas\sales_data_sample.csv", encoding="latin1")
print ("display 10 rows from top")
print (df.head(10))  
print ("display 10 rows from bottom")
print (df.tail(10))  
print (df.info())
print ("display summary statistics")

print (df.describe())
print ("describe")
print (df.shape)
print ("shape")
print (df.columns)
print ("columns")
print (df.dtypes)
print ("dtypes")




