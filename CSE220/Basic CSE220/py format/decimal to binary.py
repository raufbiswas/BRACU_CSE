# 5. Decimal to Binary(only integer value)
def decTobin(num):
    if num > 1:
        n = int(num/2)
        rem = num%2
        decTobin(n)
        print(rem,end='')
    else:
        print(num, end='')
decTobin(15)