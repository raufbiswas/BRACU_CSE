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

def commonNode(head1, head2):
    temp1 = head1
    head = Node(None)
    temp = head
    while temp1:
        temp2 = head2
        while temp2:
            if temp1.elem == temp2.elem:
                if temp.elem == None:
                    head = Node(temp1.elem)
                    temp = head
                    temp.next = temp
                else:
                    temp.next = Node(temp1.elem)
                    temp = temp.next
            temp2 = temp2.next
        temp1 = temp1.next
    return head

def printLinkedList(head):
    temp = head.next
    print(head.elem, end = " ")
    while temp:
        print("-->", temp.elem, end = " ")
        temp = temp.next
    print()

#Sample Input 01
array1 = linkedList(np.array([1, 2, 3, 4, 6]))
array2 = linkedList(np.array([2, 4, 6, 8]))
print("First linked list:")
printLinkedList(array1)
print("Second linked list:")
printLinkedList(array2)
head = commonNode(array1, array2)
print("Intersection List:")
printLinkedList(head) #Output: 2 --> 4 --> 6

#Sample Input 02
array1 = linkedList(np.array([1, 2, 3, 4, 5]))
array2 = linkedList(np.array([2, 3, 4]))
print("First linked list:")
printLinkedList(array1)
print("Second linked list:")
printLinkedList(array2)
head = commonNode(array1, array2)
print("Intersection List:")
printLinkedList(head) #Output: 2 --> 3 --> 4 