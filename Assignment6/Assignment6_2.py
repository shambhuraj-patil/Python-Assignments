
class bankaccount:
    ROI = 10.5

    def _init_(self):
        self.name = ""
        self.amount = ""
        self.interest = 0

    def accept(self):
        print("Enter the name :")
        self.name = input()

        print("Enter the amount :")
        self.amount = int(input())

    def deposit(self,value):
        self.amount = self.amount + value

    def withdraw(self,value):
        self.amount = self.amount - value

    def calculateinterest(self):
        self.interest = (self.amount * 10.5 * 1)/100

    def display(self):
        print("The account info is as below ")
        print("The name of account holder is :",self.name)
        print("The amount in account is :",self.amount)



def main():

    obj1 = bankaccount()
    obj2 = bankaccount()

    obj1.accept()
    obj2.accept()

    obj1.display()
    obj2.display()

    obj1.calculateinterest()
    obj2.calculateinterest()

    print("Amount of obj1 after ROI is :",obj1.interest )
    print("Amount of obj2 after ROI is :",obj2.interest)

    obj1.deposit(500)
    obj2.deposit(200)

    print("Amount in obj1 after deposit is ",obj1.amount)
    print("Amount in obj2 after deposit is ",obj2.amount)

    obj1.withdraw(500)
    obj2.withdraw(200)

    print("Amount in obj1 after withdrawal is ", obj1.amount)
    print("Amount in obj2 after withdrawal; is", obj2.amount)





if __name__ == "__main__":
    main()