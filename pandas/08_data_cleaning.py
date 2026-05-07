import pandas as pd

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, ot irrelevent data.
#                 ~75% of work done with Pandas is data cleaning

df = pd.read_csv("pokemon.csv", index_col="Name")

# 1. Drop irrelevent columns
# df = df.drop(columns=["Legendary", "#"])

# 2. Handle Missing data
# df = df.dropna(subset=["Type 2"])
# df = df.fillna({"Type 2": "None"})

# 3. Fix inconsistant values
# df["Type 1"] = df["Type 1"].replace({"Grass": "GRASS",
#                                      "Fire": "FIRE",
#                                      "Water": "WATER"})

# 4. Standarize text
# df["Name"] = df["Name"].str.lower()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(int)   # changes True/False to 0/1
#                                                 use bool for boolean
#                                                 use float for float

# 6. Remove duplicate
# first make sure you add dublicated entry 
# to see it effects
# df = df.drop_duplicates()

print(df.to_string())
