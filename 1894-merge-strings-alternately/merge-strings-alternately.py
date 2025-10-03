class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        new_word = []

        # Merge up to the shorter length
        for i in range(min(m, n)):
            new_word.append(word1[i])
            new_word.append(word2[i])

        # Add leftover characters (if any)
        if m > n:
            new_word.extend(word1[n:])
        else:
            new_word.extend(word2[m:])

        return ''.join(new_word)