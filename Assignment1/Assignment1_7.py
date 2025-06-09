
def ChkNum(No):
    if No % 5 == 0:
        return "True"
    else:
        return "False"
def main():
    print("Enter the number :")
    No = int(input())
    Ans = ChkNum(No)
    print(Ans)

if __name__ == "__main__":
    main()




