# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def sortedArray(n, arr):
    newArray = np.zeros(n, dtype=int)
    index = 0
    for i in range(n):
        if arr[i] > 0:
            newArray[index] = arr[i]
            index+=1
    for j in range(n):
        if arr[j] < 0:
            newArray[index] = arr[j]
            index+=1

    return newArray
N1 = 8
arr1 = np.array([1, -1, 3, 2, -7, -5, 11, 6])
returned_value = sortedArray(N1, arr1)
print(returned_value)
unittest.output_test(returned_value, np.array([1, 3, 2, 11, 6, -1, -7, -5]))

N1 = 8
arr1 = np.array([-5, 7, -3, -4, 9, 10, -1, 11])
returned_value = sortedArray(N1, arr1)
print(returned_value)
unittest.output_test(returned_value, np.array([7, 9, 10, 11, -5, -3, -4, -1]))