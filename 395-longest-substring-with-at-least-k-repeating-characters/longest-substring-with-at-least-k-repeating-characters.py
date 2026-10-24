from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        counts = Counter(s)
        for char in counts:
            if counts[char] < k:
                parts = s.split(char)
                return max(self.longestSubstring(part, k) for part in parts)

        return len(s)
