# Write a python program to sort words in alphabetical order.
def main():
	words = list(map(lambda x : x.lower(), input("Enter list of words").split()))
	words.sort()
	print(words)

if __name__ == '__main__':
	main()