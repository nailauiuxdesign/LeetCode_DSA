class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        balloon = "balloon"
        for c in text:
            if c in balloon:
                count[c] += 1
        if any(c not in count for c in balloon):
            return 0
        else:
            return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])

 
