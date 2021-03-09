import numpy as numpy
def get_input():
	r=int(input("Enter the number of rows: "))
	c=int(input("Enter the number of columns: "))
	arr=[]
	for i in range(r):
		arr.append([int(x) for x in input(f"Enter {c} numbers for row {i}: ").split()])
	return numpy.array(arr)

def main():
	arr=get_input()
	print("Matrix: ")
	print(arr)
	print("Sum of columns: ")
	print(arr.sum(axis=0))
	print("Sum of rows: ")
	print(arr.sum(axis=1))


if __name__ == "__main__":
	main()




