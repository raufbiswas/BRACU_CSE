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
#you may use this for decimal to hexadecimal mapping of 0-15
def encoding(dec_number): #0<=dec_number<=15
  return '0123456789ABCDEF'[dec_number]

def dec_to_hexa_recursive(num):
  if num//16 == 0:
    return encoding(num%16)
  else:
    return dec_to_hexa_recursive(num//16) + encoding(num%16)

print('Use of encoding function')
decimal_number = 7
print(f'Hexadecimal Number: {encoding(decimal_number)}')
decimal_number = 13
print(f'Hexadecimal Number: {encoding(decimal_number)}')

print('========1========')
returned_value = dec_to_hexa_recursive(1230)
print(f'Hexadecimal Number: {returned_value}') # This should print 4CE
unittest.output_test(returned_value, '4CE')
print('========2========')
returned_value = dec_to_hexa_recursive(600)
print(f'Hexadecimal Number: {returned_value}') # This should print 258
unittest.output_test(returned_value, '258')