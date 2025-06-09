
def Add(No1,No2):
    return No1 + No2
def main():
    print("Enter first number :")
    No1 = int(input())
    print("Enter second number :")
    No2 = int(input())

    Ans = Add(No1,No2)
    print("Addition is ",Ans)

if __name__ == "__main__":
    main()
