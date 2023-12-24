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

#Bonus Task01
def sumTree(root):
    sum = sumOfNodes(root) - root.elem
    if sum == root.elem:
        return True
    return False

def sumOfNodes(root,sum=0):
    if root != None:
        sum+=root.elem
        sum = sumOfNodes(root.left,sum)
        sum = sumOfNodes(root.right,sum)
    return sum

root = tree_construction([None,26,10,3,4,6,None,3])
print(sumTree(root))
root = tree_construction([None,40,10,5,4,6,5,10])
print(sumTree(root))
root = tree_construction([None,40,10,5,4,6,5])
print(sumTree(root))