class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        trues = [0]
        
        for i in range(1, n):
            for j in trues:
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    trues.append(i)
                    break 
                    
        return dp[-1]