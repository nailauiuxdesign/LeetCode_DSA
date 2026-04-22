from collections import deque

class Solution:
    def updateMatrix(self, mat):
        queue = deque()
        rows, cols = len(mat), len(mat[0])

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')

        while queue:
            r, c = queue.popleft()

            neighbors = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for nr, nc in neighbors:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        queue.append((nr, nc))

        return mat