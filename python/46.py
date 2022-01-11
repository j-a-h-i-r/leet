from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        self.gen(nums, [], res)
        print(res)
        return res

    def gen(self, nums, perm, res):
        if len(nums) == 0:
            res.append(perm[:])
            return
        for i in range(len(nums)):
            perm.append(nums[i])
            withoutN = nums[:i] + nums[i+1:]
            self.gen(withoutN, perm, res)
            perm.pop()
             

Solution().permute([1, 2, 3])
Solution().permute([1])
Solution().permute([0, 1])
