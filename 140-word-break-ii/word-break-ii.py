from functools import lru_cache
class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)

        @lru_cache(None)
        def dfs(text):
            if text == "":
                return [""]
            result = []

            for i in range(1, len(text) + 1):
                prefix = text[:i]
                if prefix in words:
                    for rest in dfs(text[i:]):
                        if rest == "":
                            result.append(prefix)
                        else:
                            result.append(prefix + " " + rest)
            return result

        return dfs(s)