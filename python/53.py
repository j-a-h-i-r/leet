from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        curSum = 0
        for num in nums:
            curSum += num
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0
        print(maxSum)
        return maxSum

Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
Solution().maxSubArray([1])
Solution().maxSubArray([5,4,-1,7,8])
Solution().maxSubArray([-1])