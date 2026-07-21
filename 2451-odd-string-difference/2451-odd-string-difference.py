from collections import Counter
class Solution:
    def oddString(self, words: list[str]) -> str:
        def get_pattern(word):
            pattern = []
            for i in range(1, len(word)):
                pattern.append(ord(word[i]) - ord(word[i - 1]))
            return tuple(pattern)

        patterns = []
        count = Counter()
        for word in words:
            pattern = get_pattern(word)
            patterns.append((word, pattern))
            count[pattern] += 1

        for word, pattern in patterns:
            if count[pattern] == 1:
                return word