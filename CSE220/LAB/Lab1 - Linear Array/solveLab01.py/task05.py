# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test 05: Protecc Salami
def protectSalami(salami):
    newArr = np.array([0]*len(salami), dtype = int)
    arr = np.array([0]*len(salami), dtype = int)
    index, flag = 0, False

    for i in salami:
        for j in newArr:
            if i == j:
                flag = True
        if flag == False:
            newArr[index] = i
            index+=1
        else:
            flag = False

    index = 0
    for m in newArr:
        count = 0
        for n in salami:
            if m != 0 and m == n:  
                count+=1
        arr[index] = count
        index+=1

    for x in arr:
        count = 0
        for y in arr:
            if x > 1 and x == y:
                count+=1
        if count > 1:
            return True
    
    return False

print("///  Test 05: Protecc Salami  ///")
salami = np.array([4,5,6,6,4,3,6,4])
returned_value = protectSalami(salami)
print(f'Task 5: {returned_value}') # This should print True
unittest.output_test(returned_value, True)

salami = np.array([3,4,6,3,4,7,4,6,8,6,6])
returned_value = protectSalami(salami)
print(f'Task 5: {returned_value}') # This should print False
unittest.output_test(returned_value, False)