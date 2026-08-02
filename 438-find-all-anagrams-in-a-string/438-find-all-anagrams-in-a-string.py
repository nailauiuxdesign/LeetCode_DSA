from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        count = Counter(p)
        needed = len(p)
        left = 0

        for right in range(len(s)):
            if count[s[right]] > 0:
                needed -= 1
            count[s[right]] -= 1
            if right - left + 1 > len(p):
                if count[s[left]] >= 0:
                    needed += 1
                count[s[left]] += 1
                left += 1
            if needed == 0:
                result.append(left)

        return result
