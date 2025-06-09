
def ChkNum(No):
    if No > 0:
        return "Positive"
    elif No == 0:
        return "Zero"
    else:
        return "Negative"
def main():
    print("Enter the number :")
    No = int(input())
    Ans = ChkNum(No)
    print("The number is ",Ans)
if __name__ == "__main__":
    main()




