
import threading

def even():
    print("The even numbers are :")
    for i in range(1,22,1):
        if(i % 2 == 0):
            print(i)

def odd():
    print("The odd numbers are :")
    for i in range(1,22,1):
        if (i % 2 != 0):
            print(i)

def main():
    print("Program for displaying first 10 even and odd numbers")

    p1 = threading.Thread(target=even)
    p2 = threading.Thread(target = odd)

    p1.start()
    p1.join()

    p2.start()
    p2.join()

if __name__ == "__main__":
    main()