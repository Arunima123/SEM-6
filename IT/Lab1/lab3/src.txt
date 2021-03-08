# Write a python program to implement simple calculator which perform addition,
# subtraction, multiplication, and division.
def add(a, b):
	return a+b

def sub(a, b):
	return a-b

def mul(a, b):
	return a*b

def div(a, b):
	return a/b

def main():
	a, b = [int(x) for x in input("Enter a and b: ").split()]
	print(add(a,b))
	print(sub(a,b))
	print(mul(a,b))
	print(div(a,b))

if __name__ == '__main__':
	main()