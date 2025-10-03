class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = []
        if len(word1) < len(word2):
            for i in range(len(word1)):
                new_word.append(word1[i])
                new_word.append(word2[i])
            
            new_word.append(word2[len(word1):])

        else:
            for i in range(len(word2)):
                new_word.append(word1[i])
                new_word.append(word2[i])
            
            new_word.append(word1[len(word2):])

        return ''.join(new_word)