import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

# Filterinig = keeping that match a condition

powerful_pokemon = df[df["Attack"] > 125]
High_HP_pokemon = df[df["HP"] > 175]
Legendary_pokemon = df[df["Legendary"]]
water_pokemon = df[(df["Type 1"] == "Water") |
                   (df["Type 2"] == "Water")]
Dual_type_pokemon = df[df["Type 2"].notnull() == True]

ff_pokemon = df[((df["Type 1"] == "Fire") &
                (df["Type 2"] == "Flying"))]

print(Dual_type_pokemon.to_string())
