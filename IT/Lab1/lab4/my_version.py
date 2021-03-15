print("=====QUESTION-1=====\n")
print("Enter the size of the list: ");
size=int(input())
lis=[]

print("\nEnter the elements: ");
for i in range(0,size):
    ele=int(input())
    lis.append(ele)

class py_solution1:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution1().sub_sets(lis))

print("=====QUESTION-2=====\n")
print("Enter the size of the list: ");
size1=int(input())
lis1=[]

print("\nEnter the elements: ");
for i in range(0,size1):
    ele=int(input())
    lis1.append(ele)

print("\nEnter the target: ");
target=int(input())

class py_solution2:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
print("\nIndex1 = %d and Index2  =%d" % py_solution2().twoSum(lis1,target))

print("=====QUESTION-3=====\n")
print("\nEnter the value of x: ");
x=int(input())
print("\nEnter the value of n: ");
n=int(input())

class py_solution3:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print("Pow(x,n): ")
print(py_solution3().pow(x, n));

print("=====QUESTION-4=====\n")
class py_solution4:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        print("\nEnter a string: ")
        self.str1 = input()

    def print_String(self):
        print("\nString in Upper Case: ")
        print(self.str1.upper())

str1 = py_solution4() 
str1.get_String()
str1.print_String()