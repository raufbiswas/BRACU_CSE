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
  
#Get level of a node
def getLevel(root,elem,l=0):
    if root == None:
        return 0
    if root.elem == elem:
        return l
    level = getLevel(root.left,elem,l+1)
    if level != 0:
        return level
    level = getLevel(root.right,elem,l+1)
    return level
#Array to Binary Tree
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


arr_rep = [None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None]
root = tree_construction(arr_rep)
inorder(root)
print(getLevel(root,40))