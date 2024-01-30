# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def kthSmall(n, arr, k):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr[k-1]

N1 = 6
arr1 = np.array([7, 10, 4, 3, 20, 15])
K1 = 3
returned_value = kthSmall(N1, arr1, K1)
print(returned_value)
unittest.output_test(returned_value, 7)

N2 = 5
arr2 = np.array([7, 10, 4, 20, 15])
K2 = 4
returned_value = kthSmall(N2, arr2, K2)
print(returned_value)
unittest.output_test(returned_value, 15)