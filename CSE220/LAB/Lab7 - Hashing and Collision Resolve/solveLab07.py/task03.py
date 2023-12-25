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

#Task03
class Layered_Hashtable:
  def __init__(self, express_array_size):
    self.express_array = [None] * express_array_size

  def print_express_lane(self):
    for i in self.express_array:
      print(i.elem, end = ' '*10)
    print()

  def print_layered_hashtable(self):
    print('Express Lane is:')
    self.print_express_lane()

    for i in range (len(self.express_array)-1):
      node = self.express_array[i]
      next_node = self.express_array[i+1]
      print(f'Normal Lane Nodes between Express Lane Node {node.elem} and Express Lane Node {next_node.elem} are: ')
      while node != next_node:
        print(node.elem, end = '->')
        node = node.next
      print()

    print(f'Normal Lane Nodes ending in the Express Lane Node: {node.elem}')

  #DO IT YOURSELF
  def create_layered_hashtable(self, linked_list_head):
    pos = (count(linked_list_head)//len(self.express_array))+1
    temp = linked_list_head
    cnt = 0
    while temp:
      if cnt%pos == 0:
        newTemp = temp
        self.express_array[int(cnt/pos)] = newTemp
      cnt+=1
      temp = temp.next

  #DO IT YOURSELF
  def search_element(self,k):
    arr = self.express_array
    for i in range(len(arr)-1):
      if arr[i].elem <= k < arr[i+1].elem:
        temp = arr[i]
        while temp != arr[i+1]:
          if temp.elem == k:
            return 'Found'
          temp = temp.next
      elif arr[i].elem == k or arr[i+1].elem == k:
        return 'Found'

    return 'Not Found'

arr = [4,6,9,18,25,37,62,67,79,84]
head = create_linked_list(arr)
express_array_size = 4

layered_ht = Layered_Hashtable(express_array_size)
layered_ht.create_layered_hashtable(head)
layered_ht.print_layered_hashtable()

print('==========1===========')
result = layered_ht.search_element(67)
unittest.output_test(result, 'Found')
print(f'67 {result}') #67 Found

print('==========2===========')
result = layered_ht.search_element(84)
unittest.output_test(result, 'Found')
print(f'84 {result}') #84 Found

print('==========3===========')
result = layered_ht.search_element(1)
unittest.output_test(result, 'Not Found')
print(f'1 {result}') #1 Not Found

print('==========4===========')
result = layered_ht.search_element(92)
unittest.output_test(result, 'Not Found')
print(f'92 {result}') #92 Not Found

print('==========5===========')
result = layered_ht.search_element(41)
unittest.output_test(result, 'Not Found')
print(f'41 {result}') #41 Not Found