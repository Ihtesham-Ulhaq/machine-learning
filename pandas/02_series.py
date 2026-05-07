import pandas as pd

# Series = A Pandas 1-dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet(1-dimensional)


data = [100, 102, 104]
series = pd.Series(data=data)
print(series)

data1 = [100, 102, 104]
series1 = pd.Series(data=data1, index=['a', 'b', 'c'])
print(series1)

print(series.loc[1])
print(series1.loc['a'])

series1.loc['a'] = 200
print(series1)

print(series1.iloc[0])


data2 = [100, 102, 104, 200, 202]

series2 = pd.Series(data= data2, index=['a', 'b', 'c', 'd', 'e'])

print(series2[series2 >= 200])
print()
print()
print(series2[series2 < 200])

print()
print()
print()


calories = {"Day 1": 1750,
            "Day 2": 2100,
            "Day 3": 1700}

series3 = pd.Series(data=calories)

print(series3)
series3.loc["Day 3"] += 500
print(series3.loc["Day 3"])

print(series3[series3 >= 2000])
print(series3[series3 < 2000])
