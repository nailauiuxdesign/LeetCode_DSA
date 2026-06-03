class Solution:
    def convertToTitle(self, columnNumber):
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            letter = chr(ord("A") + columnNumber % 26)
            result = letter + result
            columnNumber //= 26

        return result