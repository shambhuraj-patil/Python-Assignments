
class Demo:
    def __init__(self,a,b):
        self.No1 = a
        self.No2 = b

    def fun(self):
        return self.No1,self.No2
    def gun(self):
        return self.No1, self.No2
def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    Ans = obj1.fun()
    print("The number in fun",Ans)
    Ans = obj2.gun()
    print("The number in gun", Ans)

if __name__ == "__main__":
    main()