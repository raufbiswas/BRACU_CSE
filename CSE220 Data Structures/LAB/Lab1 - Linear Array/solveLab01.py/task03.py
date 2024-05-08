# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy
#! pip3 install levenshtein

import fhm_unittest as unittest
import numpy as np

# Test 03: Merge Lineup
def mergeLineup(pokemon_1, pokemon_2):
    result = np.array([0]*len(pokemon_1))

    for x in range (len(pokemon_1)):
        if pokemon_1[x] == None:
            pokemon_1[x] = 0

    for y in range (len(pokemon_2)):
        if pokemon_2[y] == None:
            pokemon_2[y] = 0

    for hp in range(len(pokemon_1)):
        result[hp] = pokemon_1[hp]+pokemon_2[len(pokemon_2)-1-hp]

    return result


print("///  Test 03: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None])
returned_value = mergeLineup(pokemon_1, pokemon_2)
print(f'Task 3: {returned_value}')
unittest.output_test(returned_value, np.array([12, 3, 28, -8, 5]))

pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value = mergeLineup(pokemon_1, pokemon_2)
print(f'Task 3: {returned_value}')
unittest.output_test(returned_value, np.array([4, 17, 6, 27, 2]))