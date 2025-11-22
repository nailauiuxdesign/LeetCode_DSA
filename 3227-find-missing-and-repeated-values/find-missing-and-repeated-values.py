class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        count = {}
        for row in range(N):
            for col in range(N):
                if grid[row][col] not in count:
                    count[grid[row][col]] = 0
                count[grid[row][col]] += 1
        double, missing = 0, 0

        for num in range(1, N*N + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                double = num
        return [double, missing]