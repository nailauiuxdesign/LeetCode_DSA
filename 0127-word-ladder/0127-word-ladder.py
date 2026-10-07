from collections import deque
import string

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: list[str],
    ) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            chars = list(word)
            for i in range(len(chars)):
                original = chars[i]
                for char in string.ascii_lowercase:
                    if char == original:
                        continue
                    chars[i] = char
                    next_word = ''.join(chars)
                    if next_word == endWord:
                        return steps + 1
                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, steps + 1))
                chars[i] = original

        return 0