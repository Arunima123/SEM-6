thistuple=(12, 7, 38, 56, 78 )
t=list(thistuple)
x=[]
i=0
while i<len(thistuple):
	if thistuple[i]%2==0:
		x.append(thistuple[i])
	i+=1	

y=tuple(x)	
i=0
while i<len(y):
	print y[i]
	i+=1