import numpy as np

class LinkedList:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def reverseLinkedList(head): #Outplace Reverse
    newHead = LinkedList(head.elem)
    temp = head.next

    while temp is not None:
        tempNode = LinkedList(temp.elem, newHead)
        newHead = tempNode
        temp = temp.next

    return newHead

def half_reversal_half_sum(head):
    temp, count = head, 0
    while temp:
        count += 1
        temp = temp.next

    if count == 2:
        return head

    temp, c, nHead = head, 0, None

    while temp:
        if nHead is None:
            nHead = LinkedList(temp.elem)
            nTemp = nHead
            c += 1
        elif c != (count // 2):
            nTemp.next = LinkedList(temp.elem)
            nTemp = nTemp.next
            c += 1
        else:
            break

        temp = temp.next

    nHead = reverseLinkedList(nHead)

    sum = 0
    while temp:
        sum += temp.elem
        temp = temp.next

    temp = nHead

    while temp.next:
        temp = temp.next
        
    temp.next = LinkedList(sum)

    return nHead

def createList(arr):
  head = LinkedList(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = LinkedList(arr[i])
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

head = createList(np.array([2,3,1,9,8,5]))
result = half_reversal_half_sum(head)
printLinkedList(result)