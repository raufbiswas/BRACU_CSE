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

#2
def max_recursive(arr,count = 1):
    if len(arr) == count:
        return arr[0]
    else:
        if arr[0] < arr[count]: #as -1<14 so oviously -1<25
            arr[0] = arr[count]
        return max_recursive(arr, count+1)

print('========1========')
array = np.array([14, -1, 25, 23, 7])
returned_value = max_recursive(array)
print(f'Maximum: {returned_value}') # This should print 25
unittest.output_test(returned_value, 25)
print('========2========')
array = np.array([-9, -1, -3, -3, -7])
returned_value = max_recursive(array)
print(f'Maximum: {returned_value}') # This should print -1
unittest.output_test(returned_value, -1)