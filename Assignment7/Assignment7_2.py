
import threading

def EvenFactor(No):
    print("Even factors are :")
    add = 0
    for i in range(1,No,1):
        if No % i == 0:
            if i % 2 == 0:
                print(i)
                add = add + i
    print("Addition of even factors is :",add)
    print("----------------------------------")

def OddFactor(No):
    print("Odd factors are :")
    sum = 0
    for i in range(1,No,1):
        if No % i == 0:
            if i % 2 != 0:
                print(i)
                sum = sum + i
    print("Addition of odd factors is :",sum)


def main():
    print("Program for displaying addition of even factors and odd factors")
    print("------------------------------------------------")
    print("Enter the number :")
    No = int(input())

    p1 = threading.Thread(target = EvenFactor, args = (No,))
    p2 = threading.Thread(target = OddFactor, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
