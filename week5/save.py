import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print (df)
# df.to_csv("C:\\genai-journey\\week5\\Pandas\\output.csv", index=False)
# df.to_excel("C:\\genai-journey\\week5\\Pandas\\output.xlsx", index=False, engine='openpyxl')
df.to_json("C:\\genai-journey\\week5\\Pandas\\output.json",orient="table", index=False )