class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        missing = len(t)

        l = start = 0
        min_len = float('inf')

        for r, ch in enumerate(s):
            if count[ch] > 0:
                missing -= 1
            count[ch] -= 1

            while missing == 0:
                if r - l + 1 < min_len:
                    start = l
                    min_len = r - l + 1

                count[s[l]] += 1
                if count[s[l]] > 0:
                    missing += 1
                l += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
