from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ps = []
        self.generate(n)
        print(self.ps)
        return self.ps
    def generate(self, n, opened = 0, par = ""):
        if n < 0:
            return
        if n == 0 and opened == 0:
            self.ps.append(par)
        if opened > 0:
            self.generate(n, opened - 1, par + ")")
        self.generate(n - 1, opened + 1, par + "(")
        

Solution().generateParenthesis(1)
Solution().generateParenthesis(2)
Solution().generateParenthesis(3)
