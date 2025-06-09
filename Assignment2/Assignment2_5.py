
def main():
    print("Enter the number")
    a = int(input())
    b = 0
    for i in range(2,a+1):
        if a % i == 0:
            b = b +1
    if b <=2:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")

if __name__ == "__main__":
    main()

