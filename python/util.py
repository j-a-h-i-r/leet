from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def parse(nums):
    n = len(nums)

    nodes = [None] * n
    
    i = n - 1
    while i >= 0:
        
        l = 2*i + 1
        r = 2*i + 2

        lNode = nodes[l] if l < n else None
        rNode = nodes[r] if r < n else None

        rt = TreeNode(nums[i], lNode, rNode)
        nodes[i] = rt

        i -= 1

    return nodes[0]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def parseListNode(values: List[int]):
    dummyNode = ListNode()
    dummyCopy = dummyNode
    for value in values:
        node = ListNode(value)
        dummyNode.next = node
        dummyNode = node
    return dummyCopy.next
    
def printListNode(head: ListNode):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)
