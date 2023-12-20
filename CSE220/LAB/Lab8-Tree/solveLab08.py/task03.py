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


#Task03
def inorder_predecessor(root, x):
    if x.left != None:
        x = x.left
        return right(x)
    else:
        return predecessor(root,x)
    
def right(r):
    if r.right == None:
        return r
    else:
        return right(r.right)
    
def predecessor(root,x,proot = None):
    if root.elem == x.elem:
        return proot 
    elif root.elem < x.elem:
        return predecessor(root.right,x,root)
    elif root.elem > x.elem:
        return predecessor(root.left,x,proot)

#DRIVER CODE
root = BTNode(20)
n1 = BTNode(8)
n2 = BTNode(22)
n3 = BTNode(4)
n4 = BTNode(12)
n5 = BTNode(10)
n6 = BTNode(14)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n4.left = n5
n4.right = n6

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  4 8 10 12 14 20 22
print()

x = root
print(f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}') #Inorder predecessor of node 20: 14