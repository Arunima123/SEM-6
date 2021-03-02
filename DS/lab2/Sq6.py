#Deleting rows and columns in Dataframe
import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randn(10,3),index=list('abcdefghij'),columns=list('ABC'))
print("Original Dataframe:\n",df)
df.drop('A',axis=1,inplace=True)
print("Dropping column A:\n",df)
df.drop('e',axis=0,inplace=True)
print('Dropping 5th row: using index- "e"\n',df)