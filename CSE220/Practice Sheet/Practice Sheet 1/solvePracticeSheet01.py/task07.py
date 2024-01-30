# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

def waterTrap(n, arr):
    if n < 3:
        return 0

    left, right = 0, n - 1
    leftMax, rightMax = 0, 0
    trappedWater = 0

    while left < right:
        leftMax = max(leftMax, arr[left])
        rightMax = max(rightMax, arr[right])

        if leftMax < rightMax:
            trappedWater += max(0, leftMax - arr[left])
            left += 1
        else:
            trappedWater += max(0, rightMax - arr[right])
            right -= 1

    return trappedWater

N = 6
arr = np.array([3, 0, 0, 2, 0, 4])
returned_value = waterTrap(N, arr)
print(returned_value)
unittest.output_test(returned_value, 10)