
def main():
    sum = 0
    print("Enter number")
    No = int(input())
    while(No != 0):
        Ans = No % 10
        sum = sum + Ans
        No = No // 10
    print(sum)
    
if __name__ == "__main__":
    main()