from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.gen(nums, [], res, 0)
        print(res)
        return res

    def gen(self, nums, sub, res, last):
        res.append(sub[:])

        for i in range(last, len(nums)):
            if i > last and nums[i-1] == nums[i]:
                continue

            sub.append(nums[i])
            self.gen(nums, sub, res, i+1)
            sub.pop()
    
Solution().subsetsWithDup([1,2,2])
Solution().subsetsWithDup([0])
Solution().subsetsWithDup([3,4,1,1])
