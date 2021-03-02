#Creating Dataframe using randomn values
import pandas as pd
import numpy as np
#generates 100 randomn days
dates=pd.date_range('20130101',periods=100)
df=pd.DataFrame(np.random.randn(100,4),index=dates,columns=list('ABCD'))
print(df)
print("First five records of data frame: head()")
print(df.head())
print("Last five records of data frame: tail()")
print(df.tail())
print("To print the list of index: index tuple object")
print(df.index)
print("To view column names: columns tuple")
print(df.columns)
print("Sorting by Axis: ")
print(df.sort_index(axis=1,ascending=False))
print("Slicing the rows: Displaying first 3 rows")
print(df[0:3])
print("Slicing the rows with index range: 2013-01-05 TO 2013-01-10")
print(df['20130105':'20130110'])
print("Slicing with row and Column Index: df.iloc[0]- fetches first row")
print("Third row with df.iloc[2]\n",df.iloc[2])
print('Selecting a single column of A,B,C D: "A"\n',df['A'])
print('Selecting more than one column of A,B,C D: "A" & "B"\n',df[['A','B']])
print('Selecting more than one column of A,B,C D: "A" & "B" & "C"\n',df[['A','B','C']])
print("Selecting 2 or more columns with fixed number of rows\n",df[['A','B','C']][:5])