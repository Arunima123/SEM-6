#Data frame concatenation
import pandas as pd
import numpy as np
df1=pd.DataFrame(np.random.randn(10,5),index=list('abcdefghij'),columns=list('ABCDE'))
df2=pd.DataFrame(np.random.randn(10,3),index=list('abcdefghij'),columns=list('ABC'))
print("Data Frame 1: ",df1.shape)
print("Data Frame 2: ",df2.shape)
print("Horizontal Concatenation:")
df_new=pd.concat([df1,df2],axis=1)
print('Dimensions of new Horizontal Data Frame: ',df_new.shape)
print("\nVertical Concatenation")
df_vert=pd.concat([df1,df2],axis=0)
print('Dimensions of new Vertical Data Frame: ',df_vert.shape)
print("Absent values substituted by NaN:\n",df_vert)