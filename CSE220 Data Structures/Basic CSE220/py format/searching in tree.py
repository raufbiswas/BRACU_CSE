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

#search
def search(root,key):
    if root is not None:
        if key == root.elem:
            return True
        else:
            if key < root.elem:
                return search(root.left, key)
            else:
                return search(root.right, key)
    else:
        return False
    
root = tree_construction([None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None])
print(search(root,98))