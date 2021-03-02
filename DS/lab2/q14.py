import pandas as pd
data = [['Dinesh',178,"B.Tech"],['Nithya',128,"M.Tech"],['Raji',135,"B.Tech"]]
df = pd.DataFrame(data,columns=['Name','Height','Qualification'])
address=["Ranchi","Delhi","Mumbai"]
df["Address"]=address
print df