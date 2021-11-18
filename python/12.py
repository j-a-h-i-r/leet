class Solution:
    def __init__(self):
        self.valueMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    
    def romanToInt(self, s: str) -> int:
        i, l = 0, len(s)
        totalValue = 0
        reductions = [
            ("I", "V"),
            ("I", "X"),
            ("X", "L"),
            ("X", "C"),
            ("C", "D"),
            ("C", "M"),
        ]

        while i<l:
            curRoman = s[i]
            nextRoman = s[i+1] if i+1 < l else ""

            if (curRoman, nextRoman) in reductions:
                increaseBy = self.valueMap[nextRoman] - self.valueMap[curRoman]
                totalValue += increaseBy
                i += 1
            
            else:
                totalValue += self.valueMap[curRoman]

            i += 1
        return totalValue

# leetcode examples
assert Solution().romanToInt("III")
assert Solution().romanToInt("IV")
assert Solution().romanToInt("IX")
assert Solution().romanToInt("LVIII")
assert Solution().romanToInt("MCMXCIV")
