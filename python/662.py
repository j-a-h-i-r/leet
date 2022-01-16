from util import parse, TreeNode
from typing import List, Optional
import math

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.r = {}
        self.f(root, 0, 0)
        # print(self.r)
        width = 0
        for [mn, mx] in self.r.values():
            width = max(width, mx-mn+1)

        print(width)
        return width

    def f(self, root, level, idx):
        if root is None:
            return
        
        if level not in self.r:
            self.r[level] = [math.inf, -math.inf]

        # print('idx', level, idx)
        self.r[level][0] = min(self.r[level][0], idx)
        self.r[level][1] = max(self.r[level][1], idx)

        lidx = 2*idx + 0
        ridx = 2*idx + 1

        self.f(root.left, level+1, lidx)
        self.f(root.right, level+1, ridx)



Solution().widthOfBinaryTree(parse([1,3,2,5,3,None,9]))
Solution().widthOfBinaryTree(parse([1,3,None,5,3]))
Solution().widthOfBinaryTree(parse([1,3,2,5]))