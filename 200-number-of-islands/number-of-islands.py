class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        l_row, l_col = len(grid), len(grid[0])
 
        def dfs(row, col):
            if row < 0 or row >= l_row or col < 0 or col >= l_col or grid[row][col] != "1":
                return
            else:
                grid[row][col] = "0"
                dfs(row, col + 1)
                dfs(row + 1, col)
                dfs(row, col - 1)
                dfs(row - 1, col)
 
        numIslands = 0
        for row in range(l_row):
            for col in range(l_col):
                if grid[row][col] == "1":
                    numIslands += 1
                    dfs(row, col)
 
        return numIslands