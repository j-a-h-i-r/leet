from unittest import TestCase

test = TestCase().assertEqual

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        self.singleNumber = {
            "0": "Zero",
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
        }
        self.doubleNumber = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen",
        }
        self.doubleModifier = {
            "2": "Twenty",
            "3": "Thirty",
            "4": "Forty",
            "5": "Fifty",
            "6": "Sixty",
            "7": "Seventy",
            "8": "Eighty",
            "9": "Ninety",
        }

        self.bigNumber = {
            1: "Thousand",
            2: "Million",
            3: "Billion"
        }
        
        numStr = str(num)
        numChunks = []
        for i in range(len(numStr), 0, -3):
            iStart = max(i-3, 0)
            chunk = numStr[iStart: i]
            numChunks.append(chunk)

        stringified = []

        for i, chunk in enumerate(numChunks):
            inString = self.convertUptoHundredth(chunk)
            suffix = self.bigNumber.get(i, None)
            if suffix and inString != "":
                inString = inString + " " + suffix
            if inString:
                stringified.append(inString)

        ans = " ".join(reversed(stringified))
        
        return ans
        
    def convertUptoHundredth(self, chunk: str) -> str:
        num = chunk.lstrip("0")
        if num == "":
            return ""
        if len(num) == 1:
            return self.singleNumber[num]
        if len(num) == 2:
            if num[0] == "1":
                return self.doubleNumber[num]
            if num[1] == "0":
                return self.doubleModifier[num[0]]
            return self.doubleModifier[num[0]] + " " + self.convertUptoHundredth(num[1:])
        if len(num) == 3:
            first = self.convertUptoHundredth(num[0])
            rest = self.convertUptoHundredth(num[1:])
            if rest:
                return f"{first} Hundred {rest}"
            return f"{first} Hundred"

test(Solution().numberToWords(1000000), "One Million")

test(Solution().numberToWords(0), "Zero")
test(Solution().numberToWords(10), "Ten")
test(Solution().numberToWords(20), "Twenty")
test(Solution().numberToWords(100), "One Hundred")
test(Solution().numberToWords(501), "Five Hundred One")
test(Solution().numberToWords(1000), "One Thousand")
test(Solution().numberToWords(1010), "One Thousand Ten")
test(Solution().numberToWords(10000), "Ten Thousand")
test(Solution().numberToWords(10100), "Ten Thousand One Hundred")
test(Solution().numberToWords(100000), "One Hundred Thousand")
test(Solution().numberToWords(1000000), "One Million")
test(Solution().numberToWords(10000000), "Ten Million")
test(Solution().numberToWords(100000000), "One Hundred Million")
test(Solution().numberToWords(1000000000), "One Billion")
test(Solution().numberToWords(454543), "Four Hundred Fifty Four Thousand Five Hundred Forty Three")
test(Solution().numberToWords(123), "One Hundred Twenty Three")
test(Solution().numberToWords(12345), "Twelve Thousand Three Hundred Forty Five")
test(Solution().numberToWords(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
test(Solution().numberToWords(1234567891), "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
test(Solution().numberToWords(21234567891), "Twenty One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
test(Solution().numberToWords(21234567891), "Twenty One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")
