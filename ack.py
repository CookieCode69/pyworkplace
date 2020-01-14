m = int(input("Input m: "))
n = int(input("Input n: "))

def guardian(x,y):
    check1 = x >= 0
    check2 = y >= 0

    if check1 and check2:
        checked = True
        return checked

def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        result = ack(m - 1, 1)
        return result
    elif m > 0 and n > 0:
        subresult = ack(m, n - 1)
        result = ack(m - 1, subresult)
        return result


if guardian(m,n):
    print(ack(m,n))
else:
    print("Invalid Input")
