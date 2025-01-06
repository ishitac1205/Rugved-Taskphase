import pandas as pd
df=pd.read_csv(r"/Users/ishitachoudhary/Desktop/Student Projects/Rugved/Task 2/Pandas/pokemon_data.csv")
print(df.head(4))
print(df.columns)

print(df['Type 1'][0:5])
print(df.Name )
print(df[['Name','Type 1','HP']][1:7:2])
print(df.iloc[0:5])

