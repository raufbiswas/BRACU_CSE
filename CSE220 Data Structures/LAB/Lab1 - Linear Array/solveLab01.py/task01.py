# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test 01: Play Right
def playRight(sequence, beats):
    for i in beats:
        if i == 1:
            index = len(sequence)-1
            var = sequence[index]
            for j in range(index, 0, -1):
                sequence[j] = sequence[j-1]
            sequence[0] = var
    return sequence

print("///  Test 01: Play Right  ///")
sequence = np.array([10, 20, 30, 40, 50, 60])
beats = np.array([1, 0, 0, 1, 0, 1])
returned_value = playRight(sequence, beats)
print(f'Task 1: {returned_value}')  # This should print [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, np.array([40, 50, 60, 10, 20, 30]))