class Solution:
    def reverseStr(self, s, k):
        result = ""

        for i in range(0, len(s), 2 * k):
            first = s[i:i + k]
            second = s[i + k:i + 2 * k]
            result += first[::-1]
            result += second

        return result
