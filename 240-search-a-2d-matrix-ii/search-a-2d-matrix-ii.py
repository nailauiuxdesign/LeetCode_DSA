class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            num = matrix[row][col]
            if num == target:
                return True
            elif num > target:
                col -= 1
            else:
                row += 1

        return False