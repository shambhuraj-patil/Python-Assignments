
def Disp(No):
    if (No > 0):
        print("*",end = " ")
        No = No - 1
        Disp(No)
Disp(5)