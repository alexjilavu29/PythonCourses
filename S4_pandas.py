import pandas as pd
from pandas import DataFrame
from pandas import Series

series_object = Series([1, 2, 3.5 , 'a',None], index = ['a1','a2','a3','a4','a5'])

print(series_object)
print(series_object.values)
print(series_object.index)
print(pd.isna(series_object))

data = {'Ohio':35000,"Texas":71000,"Oregon":16000,"Utah":5000}
series_data = Series(data)
print(series_data)
print(pd.notnull(series_data))

df = DataFrame(data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
],
index = ["S1","S2","S3","S4"],
columns = ["C1","C2","C3"],
dtype = float)
print(df)

print(type(df["C2"]))
print(df["C2"])
print(df.C2)
print(df.iloc[1:3,1:3])
print(df.head(3))
print(df.tail(1))
