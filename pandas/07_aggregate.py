import pandas as pd

# Aggregate functions = Reduces a set of values into a single summary value
#                       used to summarize and analyse data
#                       Often used with groupby() functions

df = pd.read_csv("pokemon.csv", index_col="Name")

# APPLIED TO WHOLE DATAFRAME
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# SINGLE COLUMN
# print(df["Attack"].mean())
# print(df["Attack"].sum())
# print(df["Attack"].min())
# print(df["Attack"].max())
# print(df["Attack"].count())

group = df.groupby("Type 1")

# print(group["Attack"].mean())
# print(group["Attack"].sum())
# print(group["Attack"].min())
# print(group["Attack"].max())
print(group["Attack"].count().to_string())
