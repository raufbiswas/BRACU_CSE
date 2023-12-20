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

def moving_around(cmds):
    grid = np.full((7, 7), '.')
    grid[3][3] = "-"
    sRow,sCol = 3 , 3
    row,col = 0 , 0
    for i in range(len(cmds)):
        if cmds[i] == 1:
            row,col = sRow-2 , sCol-3
        elif cmds[i] == 2:
            row,col = sRow-2 , sCol-1
        elif cmds[i] == 3:
            row,col = sRow-3 , sCol-2
        elif cmds[i] == 4:
            row,col = sRow-1 , sCol-2
        elif cmds[i] == 5:
            row,col = sRow-2 , sCol+1
        elif cmds[i] == 6:
            row,col = sRow-2 , sCol+3
        elif cmds[i] == 7:
            row,col = sRow-3 , sCol+2
        elif cmds[i] == 8:
            row,col = sRow-1 , sCol+2
        elif cmds[i] == 9:
            row,col = sRow+2 , sCol-3
        elif cmds[i] == 10:
            row,col = sRow+2 , sCol-1
        elif cmds[i] == 11:
            row,col = sRow+1 , sCol-2
        elif cmds[i] == 12:
           row,col = sRow+3 , sCol-2
        if row >= 0 and col >= 0:
            sRow,sCol = row,col
            grid[sRow][sCol] = "*"
    grid[sRow][sCol] = "/"
    return grid

cmds = np.array([5,11,2,9])
result = moving_around(cmds)
print_matrix(result)
#This should print
# -------------------------------------------
# |  .  |  /  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  *  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  *  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  -  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------