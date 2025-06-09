
import Arithmatic
def main():
    print("Enter First number")
    No1 = int(input())
    print("Enter Second number")
    No2 = int(input())
    Sum = Arithmatic.Add(No1,No2)
    print("Addition is ",Sum)
    Sub = Arithmatic.Sub(No1,No2)
    print("Substraction is ", Sub)
    Mult = Arithmatic.Mult(No1, No2)
    print("Multiplication is ", Mult)
    Div = Arithmatic.Div(No1, No2)
    print("Division is ", Div)
if __name__ == "__main__":
    main()