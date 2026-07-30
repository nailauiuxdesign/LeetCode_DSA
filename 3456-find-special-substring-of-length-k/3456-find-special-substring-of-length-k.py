class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        for start in range(n - k + 1):
            ch = s[start]
            same = True
            for i in range(start, start + k):
                if s[i] != ch:
                    same = False
                    break

            if not same:
                continue
                
            if start > 0 and s[start - 1] == ch:
                continue
                
            if start + k < n and s[start + k] == ch:
                continue

            return True

        return False
