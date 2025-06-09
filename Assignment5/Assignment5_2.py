
class circle:
    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
        self.PI = 3.14
    def accept(self):
        print("Enter the value of radius")
        self.radius = int(input())
        return self.radius
    def calculatearea(self):
        self.area = self.pi * self.radius * self.radius
        return self.area
    def calculatecircumference(self):
        self.circumference = 2 * self.pi * self.radius
        return self.circumference

def main():
        obj = circle()

        Ans = obj.accept()
        print("The radius is ",Ans)
        Ans = obj.calculatearea()
        print("The area is ", Ans)
        Ans = obj.calculatecircumference()
        print("The circumference is ", Ans)

if __name__ == "__main__":
    main()