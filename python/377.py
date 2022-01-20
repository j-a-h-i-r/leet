from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = {}
        ans = self.f(nums, 0, target)
        print("ans", ans)
        return ans

    def f(self, nums, i, t):
        key = f"{i}_{t}"
        if key in self.memo:
            # print("Using memo")
            return self.memo[key]
        
        if t == 0:
            # self.count += 1
            return 1
        
        if t < 0:
            return 0
        
        if i >= len(nums):
            return 0
        
        mx = 0
        for i in range(len(nums)):
            a = self.f(nums, i, t-nums[i])
            mx += a
        
        # print("mx", mx)
        self.memo[key] = mx
        return mx



Solution().combinationSum4([1,2,3], 4)
Solution().combinationSum4([9], 3)
Solution().combinationSum4([3, 5], 7)
Solution().combinationSum4([4, 2, 5], 6)
