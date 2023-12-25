class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)

def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p

#Task04
def LCA(root, x, y):
    if root==None:
        return
    if (root.elem >= x and root.elem <= y) or (root.elem >= y and root.elem <= x):
        print(root.elem)
    elif x < root.elem:
        LCA(root.left,x,y)
    else:
        LCA(root.right,x,y)

root = BTNode(15)
n1 = BTNode(10)
n2 = BTNode(25)
n3 = BTNode(8)
n4 = BTNode(12)
n5 = BTNode(20)
n6 = BTNode(30)
n7 = BTNode(6)
n8 = BTNode(9)
n9 = BTNode(18)
n10 = BTNode(22)

root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
n2.left=n5
n2.right=n6
n3.left=n7
n3.right=n8
n5.left=n9
n5.right=n10

LCA(root,6,12)
LCA(root,20,6)
LCA(root,18,22)
LCA(root,20,25)
LCA(root,10,12)