#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy

import fhm_unittest as unittest
import numpy as np

import math

class Node:
  def __init__(self, elem, next = None):
    self.elem = elem
    self.next = next

def create_linked_list(arr):
  head = Node(arr[0])
  tail = head
  for i in arr[1:]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node
  return head

#b
def nCr(n,r):
    if r == 0 or r == n:
        return 1
    else:
        return nCr(n-1, r-1) + nCr(n-1, r)
print('========1========')
returned_value = nCr(9,6)
print(f'9C6: {returned_value}') # This should print 84
unittest.output_test(returned_value, 84)
print('========2========')
returned_value = nCr(8,2)
print(f'8C2: {returned_value}') # This should print 2
unittest.output_test(returned_value, 28)
print('========3========')
returned_value = nCr(48,1)
print(f'48C1: {returned_value}') # This should print 48
unittest.output_test(returned_value, 48)