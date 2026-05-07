class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        for num in range(1, 7):
            possible = True
            for i in range(len(tops)):
                if tops[i] != num and bottoms[i] != num:
                    possible = False
                    break
            if possible:
                top_count = tops.count(num)
                bottom_count = bottoms.count(num)
                return len(tops) - max(top_count, bottom_count)
        return -1
