from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        count = Counter(s)

        for ch in t:
            if count[ch] == 0:
                return ch

            count[ch] -= 1
