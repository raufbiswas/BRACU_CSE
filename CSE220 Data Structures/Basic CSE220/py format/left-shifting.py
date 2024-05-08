def leftshift(a):
    i = 1
    while (i < len(a)):
        a[i-1] = a[i]
        i += 1
    a[len(a)-1] = None
    return a


print(leftshift([10, 20, 30, 40, 50, 60, 70, 80]))