INPUT_NUM = int(input("Type a number: "))
X = 1
Y = 0
INDEX = 0


def fibonaci(num):
    global X
    global Y
    global INDEX

    if num <= 0:
        print("invalid value!")
    elif num == 1:
        print(num)
    else:
        print(X)
        INDEX = X
        X = X + Y
        Y = INDEX
        if X == num:
            return X
        elif X > num:
            return Y
        else:
            fibonaci(num)

fibonaci(INPUT_NUM)
