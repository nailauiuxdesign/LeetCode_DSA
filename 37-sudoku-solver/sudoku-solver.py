class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    d = int(board[r][c]) - 1
                    bit = 1 << d
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def backtrack(i):
            if i == len(empty):
                return True

            r, c = empty[i]
            box = (r // 3) * 3 + c // 3
            used = rows[r] | cols[c] | boxes[box]

            for d in range(9):
                bit = 1 << d
                if not (used & bit):
                    board[r][c] = str(d + 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box] |= bit

                    if backtrack(i + 1):
                        return True

                    board[r][c] = '.'
                    rows[r] ^= bit
                    cols[c] ^= bit
                    boxes[box] ^= bit

            return False

        backtrack(0)
