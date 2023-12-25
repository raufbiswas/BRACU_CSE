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

#Full binary tree or not
def fullTree(root):
    if root == None or (root.left == None and root.right == None):
        return True
    elif root.left != None and root.right != None:
        return (fullTree(root.left) and fullTree(root.right))
    return False

root = tree_construction([None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None])
result = fullTree(root)
if result == True:
    print("Full binary tree.")
else:
    print("Not a full binary tree.")