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

#c
def count_digit_recursive(num):
    if num == 0:
        return 0
    else:
        return count_digit_recursive(num//10) + 1
returned_value = count_digit_recursive(7508)
print(f'Number of Digits: {returned_value}') # This should print 4
unittest.output_test(returned_value, 4)