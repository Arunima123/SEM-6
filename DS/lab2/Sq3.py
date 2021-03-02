#Create Dataframe using Dictionary
import pandas as pd
import numpy as np
df1=pd.DataFrame({
    'A':pd.Timestamp('20130102'),
    'B':np.array([3,2,1,3,4,5,6,7,43,4]),
    'C':pd.Categorical(['Male','Female','Male','Female','Male','Female','Male','Female','Male','Female'])
})
print(df1)
print("Number of Rows and Columns in data frame using shape tuple: ",df1.shape)
print("Display first five records: head()")
print(df1.head())
print("Display last five records: tail()")
print(df1.tail())