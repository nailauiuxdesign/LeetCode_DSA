class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        # lengths must match
        if n + m != len(s3):
            return False

        # dp[i][j] = can we form s3 using
        # first i chars of s2 and first j chars of s1
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                # take character from s1
                if j > 0:
                    if dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]:
                        dp[i][j] = True
                # take character from s2
                if i > 0:
                    if dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]:
                        dp[i][j] = True

        return dp[m][n]
