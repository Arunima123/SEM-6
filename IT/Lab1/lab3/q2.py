# Write a python program to reverse a content a file and store it in another file.
def rev(srcpath, destpath):
	with open(srcpath) as f:
		data = f.read()
	data = data[::-1]

	with open(destpath, 'w') as f:
		f.write(data)


def main():
	rev("src.txt", "text.txt")

if __name__ == '__main__':
	main()