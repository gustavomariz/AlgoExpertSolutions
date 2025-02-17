#Best Solution
def SimpleNodeDepths(root,depth=0):
  if root is None:
    return 0
  return depth + SimpleNodeDepths(root.left, depth + 1) + SimpleNodeDepths(root.right, depth + 1)

#Other solution
def nodeDepths(root):
    # Write your code here.
    sum = []
    SumDepths(root, sum, 0)
    total = 0
    for i in sum:
        total += i
    return total
    

def SumDepths(node, sum, depth):
    
    if node is None:
        return

    sum.append(depth)

    SumDepths(node.left, sum, (depth+1))
    SumDepths(node.right, sum, (depth+1))

    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
