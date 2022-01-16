from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        subs = []
        for num in nums:
            if len(subs) == 0 or num > subs[-1]:
                subs.append(num)
            else:
                pos = bisect.bisect_left(subs, num)
                subs[pos] = num
        print(len(subs))
        return len(subs)
    
Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
Solution().lengthOfLIS([0,1,0,3,2,3])
Solution().lengthOfLIS([7,7,7,7,7,7,7])
Solution().lengthOfLIS([10, 9, 11, 10, 11])
