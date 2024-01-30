# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def frequency(n, arr, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count+=1
    return count
N = 5
arr = np.array([1,1,1,1,1])
X = 1
returned_value = frequency(N, arr, X)
print(returned_value)
unittest.output_test(returned_value, 5)