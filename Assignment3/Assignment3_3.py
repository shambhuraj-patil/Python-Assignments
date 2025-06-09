
def main():
    list = []

    print("Enter how many numbers you want to store")
    No = int(input())

    print("Enter the numbers")
    for i in range(0,No):
        no = int(input())
        list.append(no)
    print(list)
    print("Maximum number is ",min(list))

if __name__ == "__main__":
    main()


