class PowerSet:
    '''Calculates all possible subsets of a list'''
    def __init__(self, arr):
        self.arr = arr
    def calculate(self, arr):
        if(len(arr) == 0):
            return [[]]
        subpowset = self.calculate(arr[:-1])
        powerset = []
        for s in subpowset:
            powerset.append(s)
            powerset.append(s + [arr[-1]])
        return powerset
    def get_powerset(self):
        return self.calculate(self.arr)
class SumToTarget:
    '''Gives the indices of the numbers that sum up to the target'''
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
    
    def get_indices(self):
        for a in range(len(self.arr)):
            for b in range(a+1, len(self.arr)):
                if(self.arr[a] + self.arr[b] == self.target):
                    return a, b
class Pow:
    '''Gives the result of pow(x, n)'''
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def calculate(self):
        return self.x ** self.n
class ToUpper:
    '''Gets string input from user and displays it in upper case'''
    def __init__(self):
        self.str = ""
    def get_String(self):
        self.str = input("Enter the string: ")
    def print_String(self):
        print("Output: ", self.str.upper())
def q1():
    arr = [int(x) for x in input("Enter the array: ").split()]
    S = PowerSet(arr)
    print("Subset = ", S.get_powerset())
def q2():
    arr = [int(x) for x in input("Enter the array: ").split()]
    target = int(input("Enter the target: "))
    S = SumToTarget(arr, target)
    print("Indices = ", S.get_indices())
def q3():
    x = int(input("Enter the base: "))
    n = int(input("Enter the exponent: "))
    P = Pow(x, n)
    print(f"{x}^{n} = {P.calculate()}")
def q4():
    U = ToUpper()
    U.get_String()
    U.print_String()
def main():
    print(    "====== Question 1 ======")
    q1()
    print("\n\n====== Question 2 ======")
    q2()
    print("\n\n====== Question 3 ======")
    q3()
    print("\n\n====== Question 4 ======")
    q4()
if __name__ == "__main__":
    main()