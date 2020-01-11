inputNum = int(input("Type a number: "))
x = 1
y = 0
index = 0


def fibonaci(num,x,y,index):
        if num <= 0:
                print("invalid value!")
        elif num == 1:
                print(num)
        else:
                print(x)
                index = x
                x = x + y
                y = index
                if x == num:
                        return x
                elif x > num:
                        return y
                else:
                        fibonaci(num,x,y,index)

fibonaci(inputNum,x,y,index)
                
                
