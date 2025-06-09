
import threading

def Small(string):
    cnt = 0
    for i in string:
        if(i.islower()):
            cnt = cnt + 1
    print("Number of small characters are :",cnt)

def Capital(string):
    cnt = 0
    for i in string:
        if(i.isupper()):
            cnt = cnt + 1
    print("Number of capital characters are :",cnt)

def Digit(string):
    cnt = 0
    for i in string:
        if(i.isdigit()):
            cnt = cnt + 1
    print("Number of digits are :",cnt)

def main():
    print("small capital digits")
    print("Enter the string :")
    string = input()

    p1 = threading.Thread(target = Small, args = (string,))
    p2 = threading.Thread(target = Capital, args = (string,))
    p3 = threading.Thread(target = Digit, args = (string,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("id of 1st thread is",id(p1))
    print("id of 1st thread is", id(p2))
    print("id of 1st thread is", id(p3))


if __name__== "__main__":
    main()