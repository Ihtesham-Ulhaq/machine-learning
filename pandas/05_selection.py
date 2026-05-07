import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

# SELECTION BY COLUMN

# print(df["Name"].to_string())
# print(df["HP"].to_string())
# print(df["Attack"].to_string())
# print(df[["Name", "HP", "Attack"]].to_string())

# SELECTION BY ROW/S

# print(df.loc["Pikachu"])
# print(df.loc["Charizard", ["HP", "Attack", "Defense", "Speed"]])
# print(df.loc["Charizard":"Blastoise", ["HP", "Attack", "Defense", "Speed"]])

# print(df.iloc[0:11])
# print(df.iloc[0:11:2])
# print(df.iloc[0:11:2, 0:3])


pokemon = input("Enter a Pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
