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

#Binary Tree to Array
arr_rep = [None]*16

def arr_cons(n,i):
    if n == None:
        return None
    else:
        arr_rep[i] = n.elem
        arr_cons(n.left, 2*i)
        arr_cons(n.right,2*i+1)

arr_rep = [None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None]
root = tree_construction(arr_rep)
inorder(root)
arr_cons(root,1)
print(arr_rep)