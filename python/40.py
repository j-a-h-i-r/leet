from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.gen(candidates, target, [], res, 0)
        print(res)
        return res

    def gen(self, nums, target, taken, res, last):
        if target < 0:
            return
        if target == 0:
            res.append(taken[:])
        
        for i in range(last, len(nums)):
            if i > last and nums[i] == nums[i-1]:
                continue
            self.gen(nums, target - nums[i], taken + [nums[i]], res, i+1)
        

Solution().combinationSum2([10,1,2,7,6,1,5], 8)
Solution().combinationSum2([2,5,2,1,2], 5)
