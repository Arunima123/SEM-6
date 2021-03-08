# Write a python program to implement binary search with recursion.
def bsearch(arr, key):
	n = len(arr)
	left = -1
	right = n-1
	while left<=right:
		mid = (left+right)//2
		if arr[mid] == key:
			return mid
		elif arr[mid] < key:
			left = mid+1
		else:
			right = mid-1
	return -1

def main():
	n = int(input("Enter n (size of list)"))
	a = list(map(int, input("Enter elements: ").strip().split()))[:n]
	key = int(input("Enter key: "))
	print(bsearch(a, key))

if __name__ == '__main__':
	main()