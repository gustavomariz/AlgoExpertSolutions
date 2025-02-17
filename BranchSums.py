# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    result = []
    calculateSums(root, 0, result)
    return result

def calculateSums(node, sum, result):

    if node is None:
        return

    sum = sum + node.value

    if node.left is None and node.right is None:
        result.append(sum)
        return

    calculateSums(node.left, sum, result)
    calculateSums(node.right, sum, result)
