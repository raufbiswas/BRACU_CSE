# 4. Reverse print a singly linked list
import numpy as np

class Node:
    def __init__(self, elem, next = None):
        self.elem, self.next = elem, next

def createLinkedList(arr):
    head = Node(arr[0])
    temp = head
    for i in arr[1:]:
        newNode = Node(i)
        temp.next = newNode
        temp = temp.next
    return head

def printLinkedList(head):
    if head.next != None:
        print(head.elem, end=' ')
        printLinkedList(head.next)


def printReverse(head):
    if head.next != None:
        printReverse(head.next)
        print(head.elem, end=' ')

array = np.array([10,20,30,40,50])
head = createLinkedList(array)
print("Original Linked List")
printLinkedList(head)
print()
print("Reversed Linked List")
printReverse(head)
print()