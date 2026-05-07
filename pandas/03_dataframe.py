import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data=data, index=["Employee 1", "Employee 2", "Employee 3"])
print(df)

print()
print()
print()

print(df.loc["Employee 1"])
print()
print()
print(df.iloc[2])
print()
print()

# add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)
print()
print()
# add a new rows
new_rows = pd.DataFrame(data=[{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                              {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])      # concat = concatination
print(df)                          # same as string concatination
print()
