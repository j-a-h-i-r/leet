from typing import List, Optional

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


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mn = -2 ** 31 - 1
        mx = 2 ** 31 + 1
        return self.check(root, mx, mn)

    def check(self, root, maxVal, minVal):
        if root is None:
            return True
        
        print(root.val, maxVal, minVal)
        if root.val is None:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False

        return (
            self.check(root.left, root.val, minVal) and
            self.check(root.right, maxVal, root.val)
        )

# print(Solution().isValidBST(parse([2,1,3])))
# print(Solution().isValidBST(parse([4,1,5,None,3,2,None])))
# print(Solution().isValidBST(parse([5,1,4,None,None,3,6])))
# print(Solution().isValidBST(parse([2,2,2])))
print(Solution().isValidBST(parse([-2147483648])))
