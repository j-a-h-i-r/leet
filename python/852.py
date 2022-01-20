from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        h = n-1

        while l < h:
            m = (l+h) // 2

            if m+1 < n:
                if arr[m] > arr[m+1]:
                    h = m
                else:
                    l = m+1
        print(l)
        return l
        
Solution().peakIndexInMountainArray([0,1,0])
Solution().peakIndexInMountainArray([0,2,1,0])
Solution().peakIndexInMountainArray([0,10,5,2])
Solution().peakIndexInMountainArray([0,1,2,3,4,3,2,1,0])
Solution().peakIndexInMountainArray([0,1,2,3,4,3])
Solution().peakIndexInMountainArray([0,1,2,4,3,2])
