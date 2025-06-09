
def Sum(No):
    if No == 0:
        return 0
    return (No % 10 + Sum(int(No / 10)))
print("Enter the number :")
No = int(input())
Result = Sum(No)
print("Sum is ",Result)
