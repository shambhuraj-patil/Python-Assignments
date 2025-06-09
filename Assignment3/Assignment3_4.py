
def main():
    list = []
    frequency = 0
    print("Enter how many numbers you want to store")
    No = int(input())

    print("Enter the numbers")
    for i in range(0,No):
        no = int(input())
        list.append(no)
    print(list)
    print("Enter the number you want to search")
    a = int(input())
    for i in list:
        if i == a:
            frequency = frequency + 1
    if (frequency > 0):
        print("frequency is ",frequency)
    else:
        print("Does not exists")

if __name__ == "__main__":
    main()


