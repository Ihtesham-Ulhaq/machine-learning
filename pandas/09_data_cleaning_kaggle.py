import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("../datasets/StudentsPerformance.csv")
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())
# print("Average Math Score:", df["math score"].mean())
# print("Highest Writing Score:", df["writing score"].max())
# df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
# print(df.columns)
# print(df.isnull().sum())

""" # Students with math score > 80:
high_math = df[df["math score"] > 80]
print(high_math.head())

# Sort by writing score:
sorted_df = df.sort_values("writing score", ascending=False)
print(sorted_df.head())
 """

###########

""" # Average scores grouped by gender:
print(df.groupby("gender")[["math score", "reading score",
                            "writing score"]].mean())
print()
print()
# Average math score by parental education:
print(df.groupby("parental level of education")["math score"].mean()) """

###################

""" # Distribution of math scores:
plt.hist(df["math score"], bins=10, edgecolor='black')
plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()
 """

################

""" sns.boxplot(x=df["reading score"])
plt.title("Reading Score Boxplot")
plt.show()
 """
#########

""" # Relationship between reading and writing:
plt.scatter(df["reading score"], df["writing score"])
plt.title("Reading vs Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.show()
 """

########

""" # Average score by gender:
sns.barplot(x="gender", y="math score", data=df)
plt.title("Average Math Score by Gender")
plt.show()
 """

#############
""" numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
 """

###########

# Save high scoring students to a new CSV file:
filtered = df[df["math score"] > 90]
filtered.to_csv("high_math_students.csv", index=False)
print("File Saved Successfully")
