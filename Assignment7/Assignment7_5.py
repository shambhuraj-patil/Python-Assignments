
import threading

def Thread1():
    for i in range(1,51,1):
        print(i)

def Thread2():
    for i in range(50,0,-1):
        print(i)

def main():
    print("Display 1 to 50 on screen and in reverse order ")
    print("The serial order is as below :")
    p1 = threading.Thread(target = Thread1)
    p1.start()
    p1.join()

    print("The reverse order is as below :")
    p2 = threading.Thread(target = Thread2)
    p2.start()
    p2.join()

if __name__ == "__main__":
    main()