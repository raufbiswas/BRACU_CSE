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

#d
def check_prime_recursive(num, divisor = 2):
    if divisor == num:
        return True
    elif num % divisor == 0:
        return False
    else:
        return check_prime_recursive(num, divisor+1)
print('========1========')
returned_value = check_prime_recursive(79)
print(f'Prime: {returned_value}') # This should print True
unittest.output_test(returned_value, True)
print('========2========')
returned_value = check_prime_recursive(391)
print(f'Prime: {returned_value}') # This should print False
unittest.output_test(returned_value, False)