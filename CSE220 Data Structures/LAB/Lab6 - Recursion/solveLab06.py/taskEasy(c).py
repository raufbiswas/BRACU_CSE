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
def print_alphabets_recursive(head):
    vowels = 'aeiouAEIOU'
    if head == None:
        return
    elif head.elem in vowels:
        print(head.elem, end = ' ')
        print_alphabets_recursive(head.next)
    else:
        print_alphabets_recursive(head.next)
        print(head.elem, end =' ')

head = create_linked_list(np.array(['b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l']))
print_alphabets_recursive(head) #This will print e a u i u l f t b