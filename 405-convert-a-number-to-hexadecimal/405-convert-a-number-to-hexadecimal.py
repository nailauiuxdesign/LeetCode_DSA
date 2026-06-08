class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"

        digits = "0123456789abcdef"
        result = ""

        for _ in range(8):
            value = num & 15
            result = digits[value] + result
            num >>= 4

        return result.lstrip("0")
