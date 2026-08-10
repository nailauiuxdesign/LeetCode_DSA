class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                best_next = min(triangle[i + 1][j], triangle[i + 1][j + 1])
                triangle[i][j] += best_next

        return triangle[0][0]