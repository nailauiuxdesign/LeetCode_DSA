class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        res = []
        r1, c1 = 0, 0
        r2, c2 = m - 1, n - 1

        while len(res) < m * n:
            j = c1
            while j <= c2 and len(res) < m * n:
                res.append(matrix[r1][j])
                j += 1
            i = r1 + 1
            while i <= r2 - 1 and len(res) < m * n:
                res.append(matrix[i][c2])
                i += 1
            j = c2
            while j >= c1 and len(res) < m * n:
                res.append(matrix[r2][j])
                j -= 1
            i = r2 - 1
            while i >= r1 + 1 and len(res) < m * n:
                res.append(matrix[i][c1])
                i -= 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return res