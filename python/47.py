from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.gen(nums, [], res)
        print(res)
        return res

    def gen(self, nums, perm, res):
        if len(nums) == 0:
            res.append(perm[:])
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            perm.append(nums[i])
            without = nums[:i] + nums[i+1:]
            self.gen(without, perm, res)
            perm.pop()



Solution().permuteUnique([1,1,2])
Solution().permuteUnique([1,2,3])
Solution().permuteUnique([1,1])
Solution().permuteUnique([1])
