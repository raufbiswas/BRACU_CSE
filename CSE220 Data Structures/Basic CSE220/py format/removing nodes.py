class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

#Inorder Traversal
def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)

#Array to Binary Tree
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p

#Removing a node
def minValueNode(node):
    current = node
    while(current.left is not None): #loop down to find the leftmost leaf
        current = current.left
    return current

#Given a binary search tree and a key, this function delete the key and returns the new root

def deleteNode(root, key):
    if root is None:
        return root
    #If the key to be deleted is smaller than the root's key then it lies in left most subtree
    if key < root.elem:
        root.left = deleteNode(root.left, key)
    #If the key to be delete is gretaer than the root's key then it lies in right subtree
    elif key > root.elem:
        root.right = deleteNode(root.right, key)
    #If key is same as root's key, then this is the node to be deleted
    else:
        #Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        #Node with two children
        #Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)
        #copy the inorder successor's content to this node
        root.key = temp.elem
        root.right = deleteNode(root.right, temp.elem) #Delete the inorder successor
    return root

root = tree_construction([None,70,50,90,40,60,80,95,20,None,55,None,75,85,None,99])
print("Inorder traversal of the given tree")
inorder(root)
print("\nDelete 20")
root = deleteNode(root,20)
print("Inorder traversal of the modified tree")
inorder(root)
print("\nDelete 100")
root = deleteNode(root,100)
print("Inorder traversal of the modified tree")
inorder(root)
print("\nDelete 75")
root = deleteNode(root,75)
print("Inorder traversal of the modified tree")
inorder(root)