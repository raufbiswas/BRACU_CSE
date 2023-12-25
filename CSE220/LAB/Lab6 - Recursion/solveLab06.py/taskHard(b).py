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
def print_pattern_2(n,ns=1,i=1):
    range = n-(ns//2)
    if (ns+1)//2==n:
        print(ns)
    else:
        print_pattern(ns, i, range)
        return print_pattern_2(n,ns+2,i*2)

def print_pattern(st, i, range):
    if range==1:
        print(st)
    else:
        print(st,end=' ')
        return print_pattern(st+i, i, range-1)
print('========1========')
n = 5
print_pattern_2(n)
print('========2========')
n = 7
print_pattern_2(n)