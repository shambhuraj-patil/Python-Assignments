
def Fact(No):
    if No == 1:
        return 1
    return (No * Fact(No - 1))
print("Enter the number :")
No = int(input())
ret = Fact(No)
print("The factorial is",ret)