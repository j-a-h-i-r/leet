from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        self.f(nums, target, 0)
        print(self.count)
        return self.count
    
    def f(self, nums, target, s):
        if len(nums) == 0 and s == target:
            self.count += 1
            return
        if len(nums) == 0:
            return
        
        n = nums.pop()
        self.f(nums, target, s + n)
        self.f(nums, target, s - n)
        nums.append(n)

Solution().findTargetSumWays([1,1,1,1,1], 3)
Solution().findTargetSumWays([1], 1)