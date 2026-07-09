from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        need = Counter()

        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] += 1

        answer = ""
        for word in words:
            have = Counter(word)
            valid = True
            for ch in need:
                if have[ch] < need[ch]:
                    valid = False
                    break
            if valid:
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer