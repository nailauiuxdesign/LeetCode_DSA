from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr):
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        occurrences = count.values()
        return len(occurrences) == len(set(occurrences))
