def dfs(node,array):
    if node is None:
        return
    array.append(node.name)
    for i in range(len(node.children)):
        dfs(node.children[i], array)

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        dfs(self,array)
        return array
