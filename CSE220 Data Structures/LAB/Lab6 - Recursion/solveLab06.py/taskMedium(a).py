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
def hocBuilder(height):
  if height == 0:
    return 0
  elif height == 1:
    return 8
  else:
    return 5 + hocBuilder(height-1)

print('========1========')
returned_value = hocBuilder(0)
print(f'The number of cards required: {returned_value}') # This should print 0
unittest.output_test(returned_value, 0)
print('========2========')
returned_value = hocBuilder(1)
print(f'The number of cards required: {returned_value}') # This should print 8
unittest.output_test(returned_value, 8)
print('========3========')
returned_value = hocBuilder(8)
print(f'The number of cards required: {returned_value}') # This should print 43
unittest.output_test(returned_value, 43)