class Solution:
    def minCut(self, s):
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        cuts = [0] * n

        for end in range(n):
            cuts[end] = end
            for start in range(end + 1):
                if s[start] == s[end]:
                    if end - start <= 1 or palindrome[start + 1][end - 1]:
                        palindrome[start][end] = True
                        if start == 0:
                            cuts[end] = 0
                        else:
                            cuts[end] = min(cuts[end], cuts[start - 1] + 1)

        return cuts[-1]