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
	print("Original Matrix: ")
	print(arr)
	print("Transposed Matrix: ")
	print(arr.transpose())

if __name__ == "__main__":
	main()

