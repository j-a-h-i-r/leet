from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # extreme answers are on the edges
        l = 0
        r = len(nums)-1
        
        ans = [None] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            ls = nums[l]*nums[l]
            rs = nums[r]*nums[r]

            if ls > rs:
                ans[i] = ls
                l += 1
            else:
                ans[i] = rs
                r -= 1
        # print(ans)
        return ans


        
Solution().sortedSquares([-4,-1,0,3,10])
Solution().sortedSquares([-7,-3,2,3,11])
Solution().sortedSquares([0, 1, 2, 3])
Solution().sortedSquares([-3, -2, -1])