class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        count = 0

        for row in range(n):
            for col in range(n):
                same = True
                for i in range(n):
                    if grid[row][i] != grid[i][col]:
                        same = False
                        break
                if same:
                    count += 1

        return count