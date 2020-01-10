inputNum = int(input("Type a number: "))


def fibonaci(num):
        x = 1
        y = 0
        index = 0
        if num <= 0:
                print("invalid value!")
        elif num == 1:
                print(1)
        else:
                while x <= num:
                        print(x)
                        index = x
                        x = x + y
                        y = index

fibonaci(inputNum)
                
                
