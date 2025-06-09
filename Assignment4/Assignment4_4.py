

def Even(No):
    if No % 2 == 0:
        return True

def square(No):
    return No ** 2
def Add(a,b):
    return a + b

def filter(Data,Function_name):
    result = []
    for no in Data:
        if (Function_name(no) == True):
            result.append(no)
    return result

def map(Data,Function_name):
    result = []
    for no in Data:
        value = Function_name(no)
        result.append(value)
    return result

def reduce(Data,Function_name):
    result = []
    Ans = 0
    for no in Data:
        Ans = Function_name(Ans,no)
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

    Data_filter = filter(list,Even)
    print("Data after filter is",Data_filter)

    Data_map = map(Data_filter,square)
    print("Data after map is", Data_map)

    output = reduce(Data_map,Add)
    print("Result after reduce is", output)


if __name__ == "__main__":
    main()