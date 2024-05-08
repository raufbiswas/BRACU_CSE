# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy

import fhm_unittest as unittest
import numpy as np

#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))

def strength_difference(clubroom):
    strength_diff = np.zeros(100, dtype = int)
    index = 0
    for i in range(len(clubroom)-1):
        for j in range(i+1,len(clubroom)):
            strength_diff[index] = clubroom[i][j] - clubroom[j][i]
            index+=1
    newArray = np.zeros(index, dtype = int)
    for x in range(index):
        newArray[x] = strength_diff[x]
    strength_diff = newArray

    return strength_diff

clubroom = np.array([
[1,  2,  9,  7],
[4,  5,  1,  8],
[3,  6,  2,  7],
[2,  8,  6,  3]
])
print_matrix(clubroom)
returned_value = strength_difference(clubroom)
print('Strength Difference Array is : ', returned_value)
unittest.output_test(returned_value, np.array([-2, 6, 5, -5, 0, 1]))