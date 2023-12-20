# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test Part 2: Playing with Array and Probability
def meanArray(array):
    count = 0
    sum = 0
    for i in range(len(array)):
        sum+=array[i]
        count += 1
    mean = sum/count
    return mean

def stdevArray(array):
    import math
    mean = meanArray(array)
    count = 0
    sum = 0
    for i in range(len(array)):
        sum+=(array[i]-mean)**2
        count += 1
    stDev = math.sqrt(sum/(count-1))
    return stDev

def probableArray(array):
    mean = meanArray(array)
    stDev = stdevArray(array)
    belowStDev = mean-(1.5*stDev)
    aboveStDev = mean+(1.5*stDev)
    count = 0
    for i in range(len(array)):
        if array[i]<belowStDev or array[i]>aboveStDev:
            count+=1

    newArray = np.array([0]*count)
    count = 0
    for i in range(len(array)):
        if array[i]<belowStDev or array[i]>aboveStDev:
            newArray[count] = array[i]
            count+=1
    if len(newArray) == 0:
        return None
    else:
        return newArray

print("///  Test Part 2: Playing with Array and Probability  ///")
array = np.array([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])
print(f"The mean of the numbers is: {meanArray(array)}")
print(f"The standard deviation is: {stdevArray(array)}")
returned_value = probableArray(array)
print(f'Task Part 2: {returned_value}')
unittest.output_test(returned_value, np.array([25,-5]))