import numpy as numpy

def get_input():
	r=int(input("Enter the number of rows: "))
	c=int(input("Enter the number of columns: "))
	arr=[]
	for i in range(r):
		arr.append([int(x) for x in input(f"Enter {c} numbers for row {i}: ").split()])
	return numpy.array(arr)

def main():
	arr1=get_input()
	print("Matrix 1: ")
	print(arr1)
	arr2=get_input()
	print("Matrix 2: ")
	print(arr2)
	print("Element wise product between two matrices: ")
	print(arr1*arr2)

if __name__ == "__main__":
	main()

