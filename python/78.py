from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.r(nums[:], [], res, 0)
        # print(res)
        return res
    
    def r(self, nums, subset, res, last):        
        res.append(subset[:])

        for i in range(last, len(nums)):
            num = nums[i]
            subset.append(num)
            self.r(nums, subset, res, i+1)
            subset.pop()

        

Solution().subsets([1,2,3])
Solution().subsets([1,2])
Solution().subsets([0])
