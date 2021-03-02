#Boolean Indexing of Dataframes
import pandas as pd
import numpy as np
dates=pd.date_range('20210301',periods=10)
df=pd.DataFrame(np.random.randn(10,5),index=dates,columns=list('ABCDE'))
print("All Records with Value in column A as positive:\n",df[df.A>0])
print("Adding a sixth column:")
df['F']=['Male','Female','Male','Female','Male','Female','Male','Female','Male','Female']
print(df)
print("Replacing all values in a given column:\n")
df.loc[:,'D']=np.array([5]*len(df))
print("Replaced COLUMN 'D' with all 5\n")
print(df)
print("sorting the values by Column B:\n",df.sort_values(by='B'))