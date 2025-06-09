
def main():
    list = []
    addition = 0
    print("Enter how many numbers you want to store")
    No = int(input())

    print("Enter the numbers")
    for i in range(0,No):
        no = int(input())
        list.append(no)
        addition = addition + no
    print(list)
    print("Addition is ",addition)

if __name__ == "__main__":
    main()


