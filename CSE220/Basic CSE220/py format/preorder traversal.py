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