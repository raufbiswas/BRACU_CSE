#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy

import fhm_unittest as unittest
import numpy as np

class Node:
  def __init__(self, elem, next = None):
    self.elem, self.next = elem, next

def create_linked_list(arr):
  head = Node(arr[0])
  tail = head
  for i in arr[1:]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node
  return head

def count(head):
  count = 0
  while head != None:
    count += 1
    head = head.next
  return count

def print_linked_list(head):
  while head != None:
    print(head.elem, end = '-> ')
    head = head.next
  print('None')
  print()

#Task01
def nerdy_run(path,k):
  dup= {}
  for i in range(len(path)):
    if path[i] in dup and ((i-dup[path[i]]) <= k):
      return path[i]
    else:
      dup[path[i]] = i
  return None

def main():

  path = [6,7,8,9,5,9]
  k = 3
  result = nerdy_run(path,k)
  unittest.output_test(result, 9)
  print(f'Duplicate value within range {k} is: {result}') #Duplicate value within range 3 is: 9

  print('===================================')
  path = [6,7,8,9,5,6]
  k = 4
  result = nerdy_run(path,k)
  unittest.output_test(result, None)
  print(f'Duplicate value within range {k} is: {result}') #Duplicate value within range 4 is: None

  print('===================================')
  path = [0.21,1.21,4.67,0.21,0.45,1.9]
  k = 7
  result = nerdy_run(path,k)
  unittest.output_test(result, 0.21)
  print(f'Duplicate value within range {k} is: {result}') #Duplicate value within range 7 is: 0.21


if __name__ == "__main__":
  main()