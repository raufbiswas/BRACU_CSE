# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def nextGreater(n, arr):
    newArray = np.zeros(n, dtype=int)
    
    for i in range(n):
        j = i + 1
        while j % n != i:
            if arr[j % n] > arr[i]:
                newArray[i] = arr[j % n]
                break
            j += 1
        else:
            newArray[i] = -1

    return newArray

n = 3
arr = np.array([1, 2, 1])
array = nextGreater(n, arr)
print(list(array))
unittest.output_test(list(array), [2, -1, 2])