
class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
    def accept(self):
        print("Enter first number")
        self.value1 = int(input())
        print("Enter second number")
        self.value2 = int(input())

    def Addition(self):
        return self.value1 + self.value2

    def Substraction(self):
        return  self.value1 - self.value2

    def Multiplication(self):
        return  self.value1 * self.value2

    def Division(self):
        return  self.value1 % self.value2


def main():
    obj = Arithmatic()
    obj.accept()

    Ans = obj.Addition()
    print("The Addition is ",Ans)
    Ans = obj.Substraction()
    print("The Substraction is ",Ans)
    Ans = obj.Multiplication()
    print("The Multiplication is ",Ans)
    Ans = obj.Division()
    print("The Division is ",Ans)

if __name__ == "__main__":
    main()