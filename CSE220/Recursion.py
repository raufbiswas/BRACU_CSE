# 1. Summation
def sum(i,n):
    if i <= n:
        return i + sum(i+1,n)
    else:
        return 0
print(sum(1,5))

# 2. Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# 3. Find max and min
def array(arr,i=0):
    if i < (len(arr)-1):
        inner(arr,i,j=0) #comparing with every number of the array
        array(arr,i+1)
    return f"{arr}\nMin : {arr[0]} Max : {arr[len(arr)-1]}"

def inner(arr,i,j):
    if j < len(arr)-i-1:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        inner(arr,i,j+1)

arr = [8,5,9,4,2,10,3,1,0,-19,12,6]
print(array(arr))

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

# 5. Decimal to Binary(only integer value
def decTobin(num):
    if num > 1:
        n = int(num/2)
        rem = num%2
        decTobin(n)
        print(rem,end='')
    else:
        print(num, end='')
decTobin(15)