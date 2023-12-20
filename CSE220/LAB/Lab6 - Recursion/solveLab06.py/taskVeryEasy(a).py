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

#a
def recursive_sum(arr, idx = 0):
    if idx == len(arr):
        return 0
    else:
        return recursive_sum(arr, idx+1) + arr[idx]

arr1 = np.array([10,34,-9,1])
returned_value = recursive_sum(arr1)
print(f'Sum of an array: {returned_value}') # This should print 36
unittest.output_test(returned_value, 36)