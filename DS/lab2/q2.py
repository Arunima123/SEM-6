x = int(input('Please Enter value 1: '))
y = int(input('Please Enter value 2: '))


temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))