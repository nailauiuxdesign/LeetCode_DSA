from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)

        @lru_cache(None)
        def can_form(word):
            for i in range(1, len(word)):
                left = word[:i]
                right = word[i:]
                if left in word_set:
                    if right in word_set or can_form(right):
                        return True
            return False

        result = []
        for word in words:
            if can_form(word):
                result.append(word)

        return result