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

#Creating a BST/Inserting in a BST
def addNode(root,i):
    if i<root.elem and root.left is None:
        root.left=BTNode(i)
    elif i>root.elem and root.right is None:
        root.right=BTNode(i)
    if i<root.elem and root.left is not None:
        addNode(root.left,i)
    elif i>root.elem and root.right is not None:
        addNode(root.right,i)

lst = [71, 50, 90, 20, 98, 40, 94]
root = BTNode(lst[0])
for i in lst[1:]:
    addNode(root,i)
print(inorder(root))
print()
addNode(root,55)
print(inorder(root))