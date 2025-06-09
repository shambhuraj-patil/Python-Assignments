
def main():
    print("Enter the number")
    No1 = int(input())
    No2 = int(input())
    a = lambda No1,No2 : No1*No2
    Ans = a(No1,No2)
    print("The multiplication is",Ans)

if __name__ == "__main__":
    main()