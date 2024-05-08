# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def sortedArray(n, arr):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

N1 = 5
arr1 = np.array([0, 2, 1, 2, 0])
returned_value = sortedArray(N1, arr1)
print(returned_value)
unittest.output_test(returned_value, np.array([0, 0, 1, 2, 2]))

N2 = 3
arr2 = np.array([0, 1, 0])
returned_value = sortedArray(N2, arr2)
print(returned_value)
unittest.output_test(returned_value, np.array([0, 0, 1]))