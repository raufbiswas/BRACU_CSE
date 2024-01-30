import numpy as np

#Node Class
class Node:
    def __init__(self, elem, next = None):
        self.elem, self.next = elem, next

#Function that creates linked list from array
def linkedList(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

def movingNode(head):
    temp = head
    newTemp = head.next
    while newTemp.next:
        newTemp = newTemp.next
        temp = temp.next

    # newTemp(5)|None --> 5.next = None --> 5.next = head --> 5|1
    newTemp.next = head

    # As 5 is now connected with head, disconnect the connection with 4.
    # Else, it will be a infinite loop.
    #  4|5 --> 4.next = 5 --> 4.next = None --> 4|None
    temp.next = None

    # Till now head is 1. newTemp(5)|head(1) --> head(5)|1
    head = newTemp
    return head

def printLinkedList(head):
    temp = head.next
    print(head.elem, end = " ")
    while temp:
        print("-->", temp.elem, end = " ")
        temp = temp.next
    print()


#Sample Input 01
array = linkedList(np.array([1, 2, 3, 4, 5]))
print("Before moving:")
printLinkedList(array)
head = movingNode(array)
print("After moving:")
printLinkedList(head) #Output: 5 --> 1 --> 2 --> 3 --> 4

#Sample Input 02
array = linkedList(np.array([3, 8, 1, 5, 7, 12]))
print("Before moving:")
printLinkedList(array)
head = movingNode(array)
print("After moving:")
printLinkedList(head) #Output: 12 --> 3 --> 8 --> 1 --> 5 --> 7