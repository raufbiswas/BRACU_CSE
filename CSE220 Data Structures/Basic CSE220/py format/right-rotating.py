def rightrotate(a):
    t = a[-1]
    i = -1
    for i in range(len(a)-1, 0, -1):
        a[i] = a[i-1]
    a[0] = t
    return a


print(rightrotate([10, 20, 30, 40, 50, 60, 70, 80]))