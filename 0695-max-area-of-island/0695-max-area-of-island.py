class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
	        l_row = len(grid)
	        l_col = len(grid[0])

	        def dfs(row, col):
	            if row < 0 or row >= l_row or col < 0 or col >= l_col or grid[row][col] != 1:
	                return 0
	            else:
	                grid[row][col] = 0
	                return 1 + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row - 1, col) + dfs(row, col + 1)

	        max_area = 0
	        for row in range(l_row):
	            for col in range(l_col):
	                if grid[row][col] == 1:
	                    max_area = max(max_area, dfs(row, col))
	        return max_area 