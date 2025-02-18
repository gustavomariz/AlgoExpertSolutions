# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    node = linkedList
    nextNode = node.next
    while nextNode != None:
        while nextNode.value == node.value:
            nextNode = nextNode.next
            node.next = nextNode
            if nextNode is None:
                return linkedList
        node = node.next   
            
        
        
    return linkedList
