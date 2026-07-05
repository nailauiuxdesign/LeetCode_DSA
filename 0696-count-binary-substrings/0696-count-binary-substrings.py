class Solution:
    def countBinarySubstrings(self, s):
        previous = 0
        current = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                count += min(previous, current)
                previous = current
                current = 1
        count += min(previous, current)

        return count