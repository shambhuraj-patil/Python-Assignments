
def ChkNum(No):
    if No % 2 == 0:
        return "Even"
    else:
        return "Odd"
def main():
    print("Enter the number :")
    No = int(input())
    Ans = ChkNum(No)
    print("The number is",Ans)
if __name__ == "__main__":
    main()
