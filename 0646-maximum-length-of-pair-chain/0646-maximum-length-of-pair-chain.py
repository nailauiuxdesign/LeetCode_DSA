class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        res = 0
        last_end = float('-inf')

        for start, end in pairs:
            if start > last_end:
                res += 1
                last_end = end

        return res
