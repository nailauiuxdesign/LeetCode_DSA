from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"  # mark visited
        while queue:
            r, c, steps = queue.popleft()
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    if nr == 0 or nc == 0 or nr == rows - 1 or nc == cols - 1:
                        return steps + 1
                    queue.append((nr, nc, steps + 1))
                    maze[nr][nc] = "+" 
        return -1