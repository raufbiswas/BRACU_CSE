def rightshift(a, k):
    for i in range(len(a)-1, 0, -1):
        a[i] = a[i-k]
    a[0] = None
    return a


a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
k = 1
print(rightshift(a, k))