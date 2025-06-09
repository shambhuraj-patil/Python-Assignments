
class Bookstore:
    NoOfBooks = 0
    def __init__(self):
        self.Name = ""
        self.Author = ""
        self.NoOfBooks = self.NoOfBooks + 1
    def Accept(self):
        print("Enter the name of Book :")
        self.Name = input()
        print("Enter the name of Author :")
        self.Author = input()
    def Display(self):
        print("The name of the Book is :",self.Name)
        print("The name of the Author is :", self.Author)
        print("No of Books :", self.NoOfBooks)
def main():
    obj1 = Bookstore()
    obj2 = Bookstore()

    obj1.Accept()
    obj2.Accept()

    obj1.Display()
    obj2.Display()

if __name__ == "__main__":
    main()