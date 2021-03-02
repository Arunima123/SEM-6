#Creating a Data Frame
import pandas as pd
data=[['Dinesh',10],['Nithya',12],['Raji',13]]
df=pd.DataFrame(data,columns=['Name','Age'])
print("Normal Dataframe")
print(df)

print("\nIndexed Data Frame")
data = {'Name':['Kavitha', 'Sudha', 'Raju','Vignesh'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank-1','rank-2','rank-3','rank-4'])
print(df)