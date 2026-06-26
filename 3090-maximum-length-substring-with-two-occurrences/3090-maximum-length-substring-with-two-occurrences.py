class Solution:
    def maximumLengthSubstring(self, s):
        left = 0
        longest = 0
        count = {}

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            while count[char] > 2:
                count[s[left]] -= 1
                left += 1
            if right - left + 1 > longest:
                longest = right - left + 1

        return longest
