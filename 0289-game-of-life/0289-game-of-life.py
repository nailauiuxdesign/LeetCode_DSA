class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(rows):
            for c in range(cols):
                live = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live += board[nr][nc] & 1
                if board[r][c] == 1:
                    if live == 2 or live == 3:
                        board[r][c] |= 2
                elif live == 3:
                    board[r][c] |= 2
        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1