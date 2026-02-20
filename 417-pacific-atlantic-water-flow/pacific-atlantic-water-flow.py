from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        def bfs(queue, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):

                        visited.add((nr, nc))
                        queue.append((nr, nc))

        pacific_q, atlantic_q = deque(), deque()
        pacific_seen, atlantic_seen = set(), set()

        for c in range(cols):
            pacific_q.append((0, c))
            atlantic_q.append((rows - 1, c))
            pacific_seen.add((0, c))
            atlantic_seen.add((rows - 1, c))

        for r in range(rows):
            pacific_q.append((r, 0))
            atlantic_q.append((r, cols - 1))
            pacific_seen.add((r, 0))
            atlantic_seen.add((r, cols - 1))

        bfs(pacific_q, pacific_seen)
        bfs(atlantic_q, atlantic_seen)

        return list(pacific_seen & atlantic_seen)