import numpy as np
a = [10, 20, 30, 40]
b = np.zeros(len(a) + 1)
i = 0
while (i < len(a)):
    b[i] = a[i]
    i += 1
b[len(a)] = 6
a = b
print(a)