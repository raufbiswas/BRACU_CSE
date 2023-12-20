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
def print_pattern(n,st=1):
    if n < st:
        return
    print_num(1,st)
    return print_pattern(n,st+1)

def print_num(s,e):
    if s > e:
        print()
        return
    print(s, end=' ')
    return print_num(s+1,e)

print('========1========')
n = 5
print_pattern(n)
print('========2========')
n = 7
print_pattern(n)