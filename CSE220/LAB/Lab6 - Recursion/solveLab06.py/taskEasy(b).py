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
def compare_recursive(head,arr,idx=0):
    if head == None:
        return True
    elif head.elem != arr[idx]:
        return False
    else:
        return compare_recursive(head.next, arr, idx+1)


print('========1========')
array = np.array([10, 11, 12, 13, 14])
head = create_linked_list(np.array([10, 11, 12, 13, 14]))
returned_value = compare_recursive(head, array)
print(f'Same: {returned_value}') # This should print True
unittest.output_test(returned_value, True)
print('========2========')
array = np.array([10, 11, 12, 13, 14])
head = create_linked_list(np.array([10, 11, 17, 13, 14]))
returned_value = compare_recursive(head, array)
print(f'Same: {returned_value}') # This should print False
unittest.output_test(returned_value, False)