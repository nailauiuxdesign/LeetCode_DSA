from collections import Counter
class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
            
        count1 = Counter(word1)
        count2 = Counter(word2)
        same_letters = set(count1.keys()) == set(count2.keys())
        same_counts = sorted(count1.values()) == sorted(count2.values())
        
        return same_letters and same_counts
