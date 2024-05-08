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

def flattenList(given_list, output_list):
    if len(given_list)==1:
        if type(given_list[0])==list: #If the element is list it will call flattenList to get the element which is not list.
            return flattenList(given_list[0],output_list)
        else:
            output_list.append(given_list[0])
            return output_list
    else:
        if type(given_list[0])==list:
            flattenList(given_list[0],output_list)
            return flattenList(given_list[1:],output_list)
        else:
            output_list.append(given_list[0])
            return flattenList(given_list[1:],output_list)

given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flattenList(given_list, []) # Initial empty list is sent for update
print(output_list)
#output_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]