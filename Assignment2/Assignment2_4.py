
def main():
    print("Enter the number")
    a = int(input())
    b = 0
    print("FActors are :")
    for i in range(1,int(a/2+1)):
        if a % i == 0:
            print(i)
            b = b + i
    print("Addition of factors is ",b)
if __name__ == "__main__":
    main()





