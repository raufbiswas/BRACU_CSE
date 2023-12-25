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

#Task04 Capture the flag
def capture_the_flag(head):
    temp = head
    newHead = None
    pos = 1
    while temp:
        if temp.elem%pos == 0:
            if newHead == None:
                newHead = Node(int(temp.elem/pos))
                newTemp = newHead
            else:
                newTemp.next = Node(int(temp.elem/pos))
                newTemp = newTemp.next
        else:
            return "Linkwise"
        pos+=1
        temp = temp.next
    newTemp.next =  Node(temp)
    return newHead


print('==============Test Case 1=============')
head = createList(np.array([11,8,21,20,5,42]))
print('Original Sequence: ', end = ' ')
printLinkedList(head)
new_head = capture_the_flag(head)
print('The flag is: ', end= ' ')
if type(new_head) == str:
  print(new_head)
else:
  printLinkedList(new_head) #This should print 11→4→7→5→1→7
print()

print('==============Test Case 2=============')
head = createList(np.array([11,8,28,20,5,42]))
print('Original Sequence: ', end = ' ')
printLinkedList(head)
new_head = capture_the_flag(head)
print('The flag is: ', end= ' ')
if type(new_head) == str:
  print(new_head) #This should print Linkwise
else:
  printLinkedList(new_head)
print()