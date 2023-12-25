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

#Bonus task assemble conga line
def assemble_conga_line(conga_line, candidate_line, idx):
    tempConga, tempCandidate = conga_line, candidate_line
    count, cand = 0, 0
    newCandidate = None
    while tempConga:
        if idx == 0:
            while tempCandidate:
                if tempCandidate.elem < tempConga.elem:
                    if cand == 0:
                        newCandidate = tempCandidate
                        cand+=1
                    else:
                        if newCandidate.elem < tempCandidate.elem:
                            newCandidate = tempCandidate
                tempCandidate = tempCandidate.next
            temp = conga_line
            conga_line = newCandidate
            conga_line.next = temp
            return conga_line

        elif count == idx-1:
            while tempCandidate:
                if tempConga.next != None:
                    if tempCandidate.elem > tempConga.elem and tempCandidate.elem < tempConga.next.elem:
                        if cand == 0:
                            newCandidate = tempCandidate
                            cand+=1
                        else:
                            if newCandidate.elem < tempCandidate.elem:
                                newCandidate = tempCandidate

                else:
                    if tempCandidate.elem > tempConga.elem:
                        if cand == 0:
                            newCandidate = tempCandidate
                            cand+=1
                        else:
                            if newCandidate.elem > tempCandidate.elem:
                                newCandidate = tempCandidate
                tempCandidate = tempCandidate.next

            if newCandidate != None:
                temp = tempConga.next
                tempConga.next = newCandidate
                tempConga.next.next = temp
            count+=1

        else:
            count+=1


        tempConga = tempConga.next

    return conga_line

print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([16,2,36,52,40,77]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 3
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->40-->41-->56-->72
printLinkedList(returned_value)

print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,16,8,36,7,40,77]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 0
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 8-->10-->15-->34-->41-->56-->72
printLinkedList(returned_value)

print('==============Test Case 3=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,12,8,36,7,40,77]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 2
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->41-->56-->72
printLinkedList(returned_value)

print('==============Test Case 4=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,16,8,36,7,40,77,78]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 6
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->41-->56-->72-->77
printLinkedList(returned_value)

print('==============Test Case 5=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,16,8,36,7,40,77,78]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 7
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->41-->56-->72
printLinkedList(returned_value)

print('==============Test Case 6=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,16,8,36,7,40,77,78]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = -1
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->41-->56-->72
printLinkedList(returned_value)