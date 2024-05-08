# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy

import fhm_unittest as unittest
import numpy as np

def atm_triangle(n):
    index = 0
    newArray = np.array([None]*n)
    for i in range(1,n+1):
        array = np.zeros(i, dtype = int)
        if i <= 2:
            for j in range(i):
                array[j] = i
        else:
            for x in range(i):
                if x == 0 or x == i-1:
                    array[x] = i
                else:
                    sum = newArray[index-1][0]
                    idx = 1
                    for y in range(1, len(newArray[index-1])):
                        sum = sum + newArray[index-1][y]
                        array[idx] = sum
                        idx+=1
        newArray[index] = array
        index+=1


    return newArray

def print_without_none(matrix):
    for i in range(len(matrix)):
        for elem in range(i+1):
            print(matrix[i][elem], end= " ")
        print()


n = 5
returned_value = atm_triangle(n)
print_without_none(returned_value)
#This should print
# 1
# 2  2
# 3  4  3
# 4  7  10  4
# 5  11 21  25  5