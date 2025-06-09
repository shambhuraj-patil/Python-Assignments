
import threading

def Evenlist(list,a):
    print("Even elements are :")
    Even = []
    sum = 0
    for a in list:
        if a % 2 == 0:
            Even.append(a)
            sum = sum + a
    print("The list of even elements is :",Even)
    print("The addition of even elements is :",sum)
    print("--------------------")
def oddlist(list,a):
    print("Odd elements are :")
    Odd = []
    sum = 0
    for a in list:
        if a % 2 != 0:
            Odd.append(a)
            sum = sum + a
    print("The list of odd elements is :",Odd)
    print("The addition of odd elements is :",sum)

def main():
    print("Program for list and addition")
    print("Enter the number of inputs :")
    num = int(input())
    print("Enter the elements for the list :")
    list = []
    for i in range(0,num,1):
        a = int(input())
        list.append(a)
    print(list)
    print("--------------------")
    p1 = threading.Thread(target = Evenlist, args = (list,a))
    p2 = threading.Thread(target = oddlist, args = (list,a))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()