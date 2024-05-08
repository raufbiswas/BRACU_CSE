# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test 04: Balance your Salami
def balanceSalami(salami):
    total_salami = 0
    my_salami = 0
    sibling_salami = 0
    con = False
    for tk in salami:
        total_salami += tk

    for s in range(1, len(salami)-1):
        for j in range(s):
            my_salami += salami[j]

        for i in range(s, len(salami)):
            sibling_salami += salami[i]

        if my_salami == sibling_salami:
            con = True
        my_salami = 0
        sibling_salami = 0

    return con


print("///  Test 04: Balance Your Salami  ///")
salami = np.array([1, 1, 1, 2, 1])
returned_value = balanceSalami(salami)
print(f'Task 4: {returned_value}')
unittest.output_test(returned_value, True)

salami = [2, 1, 1, 2, 1]
returned_value = np.array(balanceSalami(salami))
print(f'Task 4: {returned_value}')
unittest.output_test(returned_value, False)

salami = [10, 3, 1, 2, 10]
returned_value = np.array(balanceSalami(salami))
print(f'Task 4: {returned_value}')
unittest.output_test(returned_value, True)