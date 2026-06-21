class Solution:
    def firstMatchingIndex(self, s):
        for i in range(len(s) // 2 + 1):
            if s[i] == s[len(s) - 1 - i]:
                return i

        return -1