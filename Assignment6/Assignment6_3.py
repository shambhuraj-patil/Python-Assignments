
class Numbers:
    def __init__(self):
        self.value = 0

    def Accept(self):
        print("Enter the value :")
        self.value = int(input())

    def ChkPrime(self):
        a = 0
        for i in range(1, self.value+1, 1):
            if self.value % i == 0:
                a = a + 1
        if a <= 2:
            print("The number is prime")
        else:
            print("The number is not prime")

    def ChkPerfect(self):
        a = 0
        for i in range(1,self.value,1):
            if self.value % i == 0:

                a = a + i
        if a == self.value:
            print("It is a perfect number")
        else:
            print("Not a perfect number")
    def Factors(self):
        print("Factors are :")
        for i in range(1, self.value, 1):
            if self.value % i == 0:
                print(i)

    def SumFactors(self):
        add = 0
        for l in range(1, self.value, 1):
            if self.value % l == 0:
                add = add + l
        print("Sum of factors is :",add)

def main():
    obj1 = Numbers()

    obj1.Accept()
    obj1.ChkPrime()
    obj1.ChkPerfect()
    obj1.Factors()
    obj1.SumFactors()

if __name__ == "__main__":
    main()