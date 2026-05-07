import pandas as pd

df = pd.read_csv("../datasets/pokemon.csv")

# print(df)
# print(df.to_string())

df1 = pd.read_json("../datasets/pokemon.json")

print(df1)
print(df.to_string())
