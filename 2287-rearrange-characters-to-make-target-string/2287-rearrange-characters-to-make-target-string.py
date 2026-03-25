from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        countS = Counter(s)
        countT = Counter(target)
        ans = float('inf')
        
        for ch in countT:
            ans = min(ans, countS[ch] // countT[ch])
        return ans
