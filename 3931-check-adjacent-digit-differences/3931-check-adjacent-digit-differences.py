class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        N = len(s) -1
        for i in range(N):
            if abs(int(s[i]) - int(s[i +1])) >2:
                return False
        return True