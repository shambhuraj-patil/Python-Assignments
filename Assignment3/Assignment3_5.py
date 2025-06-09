

import MarvellousNum

def listprime():
    list = []

    print("Enter how many numbers you want to store")
    No = int(input())
    print("Enter the numbers")
    for i in range(0,No):
        n = int(input())
        list.append(n)
    print(list)
    a = MarvellousNum.ChkPrime(list)

if __name__ == "__main__":
    listprime()




