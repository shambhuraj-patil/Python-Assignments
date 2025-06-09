

def Prime(No):
    for i in range(2,No):
        if No % i == 0:
            return False
        else:
            return True

def Mult(No):
    return No * 2
def Max(a,b):
    if a > b:
        return a
    else:
        return b
def filter(Data,Function_name):
    result = []
    for no in Data:
        if (Function_name(no) == True):
            result.append(no)
    return result

def map(Data,Function_name):
    result = []
    for no in Data:
        b = Function_name(no)
        result.append(b)
    return result

def reduce(Data,Function_name):
    Ans = 0
    for no in Data:
        Ans = Function_name(no,Ans)
    return Ans

def main():
    print("Enter how many elements you want to store")
    a = int(input())
    list = []
    print("Enter the number")
    for i in range(0,a):
        b = int(input())
        list.append(b)
    print(list)

    Data_filter = filter(list,Prime)
    print("Data after filter is",Data_filter)

    Data_map = map(Data_filter,Mult)
    print("Data after map is", Data_map)

    output = reduce(Data_map,Max)
    print("Result after reduce is", output)

if __name__ == "__main__":
    main()