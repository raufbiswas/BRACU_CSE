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

#Task02
class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    if self.search_hashtable(s) == 'Found':
      print(s,'Already Inserted. Cannot reinsert.')
      print('===============================')
      return
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(key: {head.key}, value: {head.value})', end = '-->')
        head = head.next
      print('None')
      print()
      idx += 1


  #Do by yourself
  def __hash_function(self, s):

    if len(s)%2 != 0:
      s+='N'

    for i in range(0,len(s),2):
      idx = int(f"{ord(s[i])}{ord(s[i+1])}")

    return idx%len(self.ht)


  #Do by yourself
  def search_hashtable(self, s):
    idx = self.__hash_function(s[0])
    for i in range(len(self.ht)):
      if i == idx:
        head = self.ht[i]
        temp = head
        while temp:
          if temp.key == s[0]:
            return 'Found'
          else:
            temp = temp.next
    return 'Not Found'
  
arr = [('Colt', 360), ('Cordelius', 730), ('Shelly', 300), ('Doug', 1200), ('Emz', 520), ('Bo', 580)]
ht = Hashtable(5)
ht.create_from_array(arr)
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Doug', 1200))
unittest.output_test(result, 'Found')
print(f'(Doug, 1200) {result}')

print('======================')
ht.insert(('Doug', 1200))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))
unittest.output_test(result, 'Not Found')
print(f'(Edgar, 320) {result}')

print('======================')
ht.insert(('Edgar', 320))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))
unittest.output_test(result, 'Found')
print(f'(Edgar, 320) {result}')