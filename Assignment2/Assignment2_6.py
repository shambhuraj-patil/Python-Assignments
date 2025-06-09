
def main():
    print("Enter number")
    No = int(input())

    for i in range(No+1,1,-1):
        for j in range(1,i):
            print("*",end = " ")
        print("\n")
if __name__ == "__main__":
    main()