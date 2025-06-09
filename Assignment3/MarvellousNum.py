
def ChkPrime(list):
    Mylist = []
    for i in list:
        a = 0
        sum = 0
        for j in range(1,i):
            if i % j == 0:
                a = a + 1
        if a == 1:
            b = Mylist.append(i)
        for k in Mylist:
            sum = sum + 1
    print("The prime numbers are :",Mylist)
    print(sum)




