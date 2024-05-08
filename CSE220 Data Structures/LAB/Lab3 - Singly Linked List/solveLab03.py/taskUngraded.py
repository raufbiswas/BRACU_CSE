# You must run this cell to install dependency
#! pip3 install fhm-unittest
#! pip3 install fuzzywuzzy

# You must run this cell
import fhm_unittest as unittest
import numpy as np

class Node:
  def __init__(self,elem,next = None):
    self.elem, self.next = elem,next

class LinkedList:
  def __init__(self,arr):
    self.head = Node(arr[0])
    tail = self.head
    for i in range(1,len(arr)):
      newNode = Node(arr[i])
      tail.next = newNode
      tail = newNode

  def printLinkedList(self):
    temp = self.head
    while temp != None:
      if temp.next != None:
        print(temp.elem, end = '-->')
      else:
        print(temp.elem)
      temp = temp.next

#-----------------------------------------------Nodes Count-----------------------------------------------
  def countNodes(self):
    count = 0
    temp = self.head
    while temp:
      count+=1
      temp = temp.next
    return count
#-----------------------------------------------Nodes Count-----------------------------------------------

#-----------------------------------------Node At a Certain Index-----------------------------------------
  def nodeAt(self, idx):
    temp = self.head
    count = 0
    node = None
    while temp:
      if count == idx:
        node = temp
        break
      count += 1
      temp = temp.next
    return node
#-----------------------------------------Node At a Certain Index-----------------------------------------

#---------------------------------------Element At a Certain Index----------------------------------------
  def elemAt(self,idx):
    temp = self.head
    count = 0
    elem = None
    while temp:
      if count == idx:
        elem = temp.elem
        break
      count += 1
      temp = temp.next
    return elem
#---------------------------------------Element At a Certain Index----------------------------------------

#-------------------------------------------Index of an Element-------------------------------------------
  def indexOf(self,value):
    temp = self.head
    count = 0
    while temp:
      if temp.elem == value:
        return count
      count+=1
      temp = temp.next
    return -1
#-------------------------------------------Index of an Element-------------------------------------------

#----------------------------------Linked List Contains an Element or Not---------------------------------
  def contains(self,value):
    temp = self.head
    while temp:
      if temp.elem == value:
        return True
      temp = temp.next
    return False
#----------------------------------Linked List Contains an Element or Not---------------------------------

#-----------------------------------------Insert Value at an Index----------------------------------------
  def insert(self, value, idx):
    newNode = Node(value)
    if idx == 0:
      newNode.next = self.head
      self.head = newNode
    else:
      prev = self.nodeAt(idx-1)
      if prev != None:
        newNode.next = prev.next
        prev.next = newNode
#-----------------------------------------Insert Value at an Index----------------------------------------

#-----------------------------------------Remove Value From an Index----------------------------------------
  def remove(self,idx):
    if idx == 0:
      self.head = self.head.next
    else:
      prev = self.nodeAt(idx-1)
      if prev != None:
        prev.next = prev.next.next
#-----------------------------------------Remove Value From an Index----------------------------------------

#------------------------------------------------Right Rotate-----------------------------------------------
  def rotateRight(self):
    tail = self.head
    temp = tail.next
    while temp.next:
      temp = temp.next
      tail = tail.next
    temp.next = self.head
    tail.next = None
    self.head = temp
    
#------------------------------------------------Right Rotate-----------------------------------------------

#-------------------------------------------------Left Rotate-----------------------------------------------
  def rotateLeft(self):
    head = self.head
    temp = head.next
    while temp:
      t = temp
      temp = temp.next
    t.next = head
    self.head = head.next
    head.next = None
#-------------------------------------------------Left Rotate-----------------------------------------------




print('Create Linked List')
l1 = LinkedList(np.array([10,34,21,6,-2]))
l1.printLinkedList()
print()

print('Count Nodes of Linked List')
print(l1.countNodes())
print()

print('Find out the node at a certain index')
n = l1.nodeAt(3)
print('Node at index 3:', end = ' ')
print(n.elem if n!=None else 'Invalid Index')
print('Corner Cases:')
print('Node at index -1:', end = ' ')
n = l1.nodeAt(-1)
print(n.elem if n!=None else 'Invalid Index')
print('Node at index 5:', end = ' ')
n = l1.nodeAt(5)
print(n.elem if n!=None else 'Invalid Index')
print()

print('Find out the element at a certain index')
print('Element at index 1:', end = ' ')
print(l1.elemAt(1))
print('Corner Cases:')
print('Element at index -2:', end = ' ')
print(l1.elemAt(-2))
print('Element at index 6:', end = ' ')
print(l1.elemAt(6))
print()

print('Find out the index of an element')
print('Index of element -2', end = ' ')
print(l1.indexOf(-2))
print('Corner Cases:')
print('Index of element 23', end = ' ')
print(l1.indexOf(23))
print()

print('Find out the if linked list contains an element')
print('Linked List contains -2:', end = ' ')
print(l1.contains(-2))
print('Corner Cases:')
print('Linked List contains 3:', end = ' ')
print(l1.contains(3))
print()

print('Insert element in certain index')
print('Insert 41 at index 2:', end = ' ')
l1.insert(41,2)
l1.printLinkedList()
print('Corner Cases:')
print('Insert 25 at index 0:', end = ' ')
l1.insert(25,0)
l1.printLinkedList()
print('Insert 15 at index 7:', end = ' ')
l1.insert(15,7)
l1.printLinkedList()
print('Insert 27 at index -1:', end = ' ')
l1.insert(27,-1)
l1.printLinkedList()
print()

print('Delete node from a certain index')
print('Delete from index 5:', end = ' ')
l1.remove(5)
l1.printLinkedList()
print('Corner Cases:')
print('Delete from index 0:', end = ' ')
l1.remove(0)
l1.printLinkedList()
print('Delete from index 5:', end = ' ')
l1.remove(5)
l1.printLinkedList()
print('Delete from index -1:', end = ' ')
l1.remove(-1)
l1.printLinkedList()
print()

print('Right Rotate')
l1.rotateRight()
l1.printLinkedList()
print()

print('Left Rotate')
l1.rotateLeft()
l1.printLinkedList()
print()