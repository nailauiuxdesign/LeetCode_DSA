class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        s = []

        # Merge while both have characters
        for i in range(min(A, B)):
            s.append(word1[i])
            s.append(word2[i])

        # Append leftovers (if any)
        if A > B:
            s.extend(word1[B:])
        else:
            s.extend(word2[A:])

        return ''.join(s)