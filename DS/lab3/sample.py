#Usage of for loop mapping by value
#calculate sum of all elements in a 2D numpy array
import numpy as np
a=np.array(((3,2,9),(1,6,7)))
s1=0;
for row in a:
    for col in row:
        s1=s1+col
print(s1)

#Usage of for loop mapping by index
#calculate sum of all elements in a 2D numpy array (iterate over range)
s=0;
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        s=s+a[i,j]
print(s)