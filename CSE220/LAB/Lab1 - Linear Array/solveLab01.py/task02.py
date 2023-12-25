# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test 02: Discard Cards
def discardCards(cards,number):
    num = 0
    while num < len(cards):
        if cards[num] == number:
            for i in range(num+1, len(cards)):
                cards[i-1] = cards[i]
            cards[len(cards)-1] = 0
        else:
            num+=1
    return cards


print("///  Test 02: Discard Cards  ///")
cards = np.array([1,2,3,2,8,2,2,5,7])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1, 3, 8, 5, 7, 0, 0, 0, 0]
unittest.output_test(returned_value, np.array([1, 3, 8, 5, 7, 0, 0, 0, 0]))