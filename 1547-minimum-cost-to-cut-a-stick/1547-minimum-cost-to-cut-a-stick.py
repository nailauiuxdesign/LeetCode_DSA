from functools import lru_cache

class Solution:
    def minCost(self, n, cuts):
        cuts = [0] + sorted(cuts) + [n]
        @lru_cache(None)
        def dfs(left, right):
            if right - left <= 1:
                return 0

            best = float("inf")
            for cut in range(left + 1, right):
                cost = cuts[right] - cuts[left]
                cost += dfs(left, cut)
                cost += dfs(cut, right)
                best = min(best, cost)
            return best

        return dfs(0, len(cuts) - 1)
