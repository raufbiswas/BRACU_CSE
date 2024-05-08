# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test 06: Odd Even Wave
def waveYourFlag(arr):
    newArray = np.array([0]*len(arr))
    index = 0
    newArray[0] = arr[0]

    for i in range(1, len(arr)):

        if newArray[index] % 2 == 0:
            index += 1

            for j in range(i, len(arr)):

                if arr[j] % 2 != 0:
                    newArray[index] = arr[j]
                    arr[j], arr[i] = arr[i], arr[j]
                    break

        else:
            index += 1

            for j in range(i, len(arr)):

                if arr[j] % 2 == 0:
                    newArray[index] = arr[j]
                    arr[j], arr[i] = arr[i], arr[j]
                    break

    return newArray


print("///  Test 06: Odd Even Wave  ///")
arr = np.array([2, 12, 3, 8, 1, 5])
returned_value = waveYourFlag(arr)
print(f'Task 6: {returned_value}')  # This should print [2,3,12,1,8,5]
unittest.output_test(returned_value, np.array([2, 3, 12, 1, 8, 5]))

arr = np.array([45, 23, 78, 84, 41])
returned_value = waveYourFlag(arr)
print(f'Task 6: {returned_value}')  # This should print [45,78,23,84,41]
unittest.output_test(returned_value, np.array([45, 78, 23, 84, 41]))