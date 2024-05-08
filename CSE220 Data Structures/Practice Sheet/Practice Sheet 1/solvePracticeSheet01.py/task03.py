# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def subArray(n, s, a):
    newArray = np.zeros(2, dtype=int)
    sum = 0
    start = 0
    while start <= n:
        for i in range(start, n):
            sum+=a[i]
            if sum == s:
                newArray[0] = a[start]
                newArray[1] = a[i]
                return newArray

        start+=1
        sum = 0

N1 = 5
S1 = 12
A1 = np.array([1,2,3,7,5])
returned_value = subArray(N1,S1,A1)
print(returned_value)
unittest.output_test(returned_value, np.array([2, 7]))

N2 = 10
S2 = 15
A2 = np.array([1,2,3,4,5,6,7,8,9,10])
returned_value = subArray(N2,S2,A2)
print(returned_value)
unittest.output_test(returned_value, np.array([1, 5]))