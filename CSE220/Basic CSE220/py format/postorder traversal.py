class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

#Postorder Traversal
def postorder(root):
  if root == None:
    return
  postorder(root.left)
  postorder(root.right)
  print(root.elem, end = ' ')