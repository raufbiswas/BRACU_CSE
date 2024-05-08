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

def create_fence(district, depth):
    district_row, district_col = district.shape

    newCol = np.array([8]*(district_col+(depth*2)), dtype = int)
    newArray = np.array([newCol]*(district_row+(depth*2)))

    for i in range(district_row):
        for j in range(district_col):
            newArray[i+depth][j+depth]=district[i][j]

    return newArray

depth = 1
district = np.array([[2,3,4], [3,4,6], [2,1,4]])
print_matrix(district)
ans = create_fence(district, depth)
print_matrix(ans)
#This will print
# |  8  |  8  |  8  |  8  |  8  |
# -------------------------------
# |  8  |  2  |  3  |  4  |  8  |
# -------------------------------
# |  8  |  3  |  4  |  6  |  8  |
# -------------------------------
# |  8  |  2  |  1  |  4  |  8  |
# -------------------------------
# |  8  |  8  |  8  |  8  |  8  |
# -------------------------------
print('################')
depth = 2
district = np.array([
                 [2,3,4,1],
                 [3,4,6,5],
                 [2,1,4,7]
                ])
print_matrix(district)
ans = create_fence(district, depth)
print_matrix(ans)