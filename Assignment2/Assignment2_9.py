
def main():
    a = 0
    print("Enter number")
    No = int(input())

    while(No != 0):
        No = No // 10
        a = a + 1
    print(a)
    
if __name__ == "__main__":
    main()