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

#predecessor
def inorder_predecessor(root, x):
    if x.left != None:
        return rightmost(x.left)
    return predecessor(root,x)

def rightmost(root):
    if root.right != None:
        return rightmost(root.right)
    return root

def predecessor(root, x, parent = None):
    if root.elem == x.elem:
        return parent
    elif root.elem < x.elem:
        return predecessor(root.right, x, root)
    else:
        return predecessor(root.elem, x, parent)
    
root = tree_construction([None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None])
print(inorder_predecessor(root,root).elem)