from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combs = [""]
        new_combs = []

        for digit in digits:
            new_combs = []
            for ch in char[digit]:
                for comb in combs:
                    print(comb+ch)
                    new_combs.append(comb + ch)
            combs = new_combs
        print(combs)
        return combs

Solution().letterCombinations("23")
Solution().letterCombinations("2345")
Solution().letterCombinations("")
