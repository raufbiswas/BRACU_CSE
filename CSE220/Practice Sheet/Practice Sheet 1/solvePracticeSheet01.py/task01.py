# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def unionSet(size, a, b):
    length = size[0]+size[1]
    array = np.zeros(length, dtype=int)
    index = 0

    for i in range(len(a)):
        array[index] = a[i]
        index += 1
    count = 0
    for j in range(len(b)):
        for k in range(len(a)):
            if (b[j] == a[k]) and (a[k] != 0):
                count = 1
        if count == 0:
            array[index] = b[j]
            index += 1
        count = 0
    return index


size1 = np.array([5, 3])
a1 = np.array([1, 2, 3, 4, 5])
b1 = np.array([1, 2, 3])
returned_value = unionSet(size1, a1, b1)
print(returned_value)
unittest.output_test(returned_value, 5)

size2 = np.array([6, 2])
a2 = np.array([85, 25, 1, 32, 54, 6])
b2 = np.array([85, 2])
returned_value = unionSet(size2, a2, b2)
print(returned_value)
unittest.output_test(returned_value, 7)