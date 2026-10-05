class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0

        for r in range(rows):
            prev = 0
            for c in range(1, cols + 1):
                old = dp[c]
                if matrix[r][c - 1] == "1":
                    dp[c] = min(dp[c], dp[c - 1], prev) + 1
                    max_side = max(max_side, dp[c])
                else:
                    dp[c] = 0
                prev = old

        return max_side * max_side