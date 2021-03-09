import numpy as np

def a():
	arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("A:\nList:")
	print(arr)
	print("Numpy array:")
	print(np.array(arr, dtype=float))
	print()

def b():
	tpl = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	print("B:\nTuple:")
	print(tpl)
	print("Numpy array:")
	print(np.array(tpl))
	print()

def c():
	print("C:\nNumpy array:")
	print(np.zeros((3,4)))

def d():
	print("D:\nSequence:")
	print(np.arange(0, 20, 5))

def e():
	arr = np.random.randint(10, size=(3,4))
	print("E:\nOriginal array:")
	print(arr)
	print("Modified array:")
	print(arr.reshape(2, 2, 3))

def f():
	arr = np.random.randint(10, size=(3,4))
	print("F:\nArray:")
	print(arr)
	print(f"Overall : Max: {arr.max()}\t Min: {arr.min()}\t\t Sum: {arr.sum()}")
	print(f"Col-wise: Max: {arr.max(axis=0)} Min: {arr.min(axis=0)}\t Sum: {arr.sum(axis=0)}")
	print(f"Row-wise: Max: {arr.max(axis=1)}\t Min: {arr.min(axis=1)}\t Sum: {arr.sum(axis=1)}")

def main():
	a()
	print()
	b()
	print()
	c()
	print()
	d()
	print()
	e()
	print()
	f()

if __name__ == "__main__":
	main()