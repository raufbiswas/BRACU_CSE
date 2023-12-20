# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy

import fhm_unittest as unittest
import numpy as np

#Run this cell
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()

#Task02 check similarity
def check_similar(building_1, building_2):
    similarity = "Similar"
    while building_1 != None and building_2 != None:
        if building_1.elem != building_2.elem:
            break
        building_1 = building_1.next
        building_2 = building_2.next
    if building_1 != None or building_2 != None:
        similarity = "Not Similar"
    return similarity
print('==============Test Case 1=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Similar'
unittest.output_test(returned_value, 'Similar')
print()

print('==============Test Case 2=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 3=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()

print('==============Test Case 4=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
unittest.output_test(returned_value, 'Not Similar')
print()