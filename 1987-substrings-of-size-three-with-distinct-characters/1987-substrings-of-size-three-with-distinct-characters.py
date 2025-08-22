class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s) - 2):
            c1, c2, c3 = s[i], s[i+1], s[i+2]
            if c1 != c2 and c1 != c3 and c2 != c3:
                count += 1
        return count
