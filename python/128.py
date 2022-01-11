from typing import List
from unittest import TestCase

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = False

        longest = 0
        
        for num in d:
            if num-1 not in d:
                nextNum = num+1
                while nextNum in d:
                    nextNum += 1

                longest = max(longest, nextNum-num)
        return longest

test = TestCase().assertEqual

test(Solution().longestConsecutive([100,4,200,1,3,2]), 4)
test(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
