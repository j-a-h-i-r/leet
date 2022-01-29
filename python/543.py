from typing import Optional
from util import TreeNode, parse

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        self.f(root)
        print(self.mx)
        return self.mx
        
    def f(self, root):
        if not root:
            return 0

        l, r = 0, 0
        if root.left:
            l = 1
        if root.right:
            r = 1

        l += self.f(root.left)
        r += self.f(root.right)
        if l + r > self.mx:
            self.mx = l + r
        # print(l, r)
        return max(l, r)
        

Solution().diameterOfBinaryTree(parse([1,2,3,4,5]))
Solution().diameterOfBinaryTree(parse([1,2]))