from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []
        n = len(s)

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start: int):
            if start == n:
                result.append(part.copy())
                return

            for end in range(start, n):
                if is_palindrome(start, end):
                    part.append(s[start:end + 1])
                    dfs(end + 1)
                    part.pop()

        dfs(0)
        return result
