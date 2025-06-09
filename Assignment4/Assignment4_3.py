
def Check(No):
    if (No >=70 and No<=90):
        return True
    else:
        return False
def Increase(No):
    return No + 10
def Product(a,b):
    return a*b

def filterX(Data,Function_name):
    result = []
    for no in Data:
        if (Function_name(no) == True):
            result.append(no)
    return result

def mapX(Data,Function_name):
    result = []
    for no in Data:
        b = Function_name(no)
        result.append(b)
    return result

def reduceX(Data,Function_name):
    Ans = 1
    for no in Data:
        Ans = Function_name(Ans,no)
    return Ans

def main():
    print("Enter how many elements you want to store")
    a = int(input())

    Data1 = []
    print("Enter the number")
    for i in range(0,a):
        b = int(input())
        Data1.append(b)
    print("Data is ",Data1)

    Data_filter = filterX(Data1,Check)
    print("Data after filter is",Data_filter)

    Data_map = mapX(Data_filter,Increase)
    print("Data after map is", Data_map)

    output = reduceX(Data_map,Product)
    print("Result after is", output)


if __name__ == "__main__":
    main()