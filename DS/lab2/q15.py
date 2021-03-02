import pandas as pd
data = [['Dinesh',178,"B.Tech"],['Nithya',128,"M.Tech"],['Raji',135,"B.Tech"]]
df = pd.DataFrame(data,columns=['Name','Height','Qualification'])
df.insert(3,"roll",[3,5,6])
print df
