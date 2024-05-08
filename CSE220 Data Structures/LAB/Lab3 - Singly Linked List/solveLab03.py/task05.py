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

#Task05 Shuffle On Song
def shuffle_on_song(head):
    temp = head
    newHead = None
    while temp:
        if ord(temp.elem)%2 == 0:
            if newHead == None:
                newHead = Node(temp.elem)
                newTemp = newHead
            else:
                newTemp.next = Node(temp.elem)
                newTemp = newTemp.next
        temp = temp.next
    
    temp = head
    while temp:
        if ord(temp.elem)%2 != 0:
            if newHead == None:
                newHead = Node(temp.elem)
                newTemp = newHead
            else:
                newTemp.next = Node(temp.elem)
                newTemp = newTemp.next
        temp = temp.next

    return newHead

print('==============Test Case 1=============')
head = createList(np.array(['S','E','N','P','A','I']))
print('Original Play List: ', end = ' ')
printLinkedList(head)
newhead =  shuffle_on_song(head)
print('New Play List: ', end = ' ')
printLinkedList(newhead) #This should print N-->P-->S-->E-->A-->I
print()

print('==============Test Case 2=============')
head = createList(np.array(['N','I','S','H','I','N','O','Y','A']))
print('Original Play List: ', end = ' ')
printLinkedList(head)
newhead =  shuffle_on_song(head)
print('New Play List: ', end = ' ')
printLinkedList(newhead) #This should print N-->H-->N-->I-->S-->I-->O-->Y-->A
print()