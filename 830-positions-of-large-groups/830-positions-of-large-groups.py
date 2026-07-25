class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        start = 0

        for end in range(len(s)):
            if end == len(s) - 1 or s[end] != s[end + 1]:
                if end - start + 1 >= 3:
                    result.append([start, end])
                start = end + 1

        return result
