class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()
        queens = []

        def backtrack(row: int):
            if row == n:
                board = []
                for c in queens:
                    board.append("." * c + "Q" + "." * (n - c - 1))
                res.append(board)
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                queens.append(col)

                backtrack(row + 1)

                queens.pop()
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        backtrack(0)
        return res
