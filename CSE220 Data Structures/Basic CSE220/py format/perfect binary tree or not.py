class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

#Array to Binary Tree
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p

#Get depth of a node
def calDepth(root):
    if root == None:
        return 0
    return 1+calDepth(root.left)

#Perfect Binary Tree or not
def perfectTree(root,l=0):
    d = calDepth(root)
    if root == None:
        return True
    if (root.left == None and root.right == None):
        return (d == l+1)
    elif (root.left is None or root.right is None):
        return False
    return(perfectTree(root.left,l+1) and perfectTree(root.right,l+1))

root = tree_construction([None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None])
result = perfectTree(root)

if result:
    print("Perfect binary tree")
else:
    print("Not a perfect binary tree")