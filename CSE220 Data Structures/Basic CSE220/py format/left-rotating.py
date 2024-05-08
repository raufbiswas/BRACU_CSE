import numpy as np
def leftrotate(a):
    t = a[0]
    i = 1
    while (i < len(a)):
        a[i-1] = a[i]
        i += 1
    a[len(a)-1] = t
    return a


print(leftrotate(np.array([10, 20, 30, 40, 50, 60, 70, 80])))