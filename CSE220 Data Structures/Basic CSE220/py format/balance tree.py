class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

#Preorder Traversal
def preorder(root):
  if root == None:
    return
  print(root.elem, end = ' ')
  preorder(root.left)
  preorder(root.right)

#Array to Binary Tree
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p

#Appends into a list with tree nodes using inorder traversal
def pushTreeNodes(root, arr):
    if root is None:
        return
    pushTreeNodes(root.left, arr)
    arr.append(root)
    pushTreeNodes(root.right, arr)
#Recursive function to construct a height-balanced tree given nodes in sorted order

def buildBalancedBST(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 #find the middle index
    root = arr[mid] #The root node will be a node present at the mid-index recursively construct left and right subtree
    root.left = buildBalancedBST(arr, start, mid - 1)
    root.right = buildBalancedBST(arr, mid + 1, end)
    return root

root = tree_construction([None,40,None,50,None,None,None,70])
print(f"Unbalanced State Pre-Order:")
preorder(root)
arr = []
pushTreeNodes(root, arr)
newRoot = buildBalancedBST(arr, 0, len(arr) - 1)
print("\nBalanced State Pre-Order:")
preorder(newRoot)