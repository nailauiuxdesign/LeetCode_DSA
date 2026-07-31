from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        max_odd = 0
        min_even = len(s)

        for freq in count.values():
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even