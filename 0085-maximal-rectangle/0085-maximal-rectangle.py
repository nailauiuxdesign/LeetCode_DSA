
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        heights = [0] * len(matrix[0])
        max_area = 0

        for row in matrix:
            for i, cell in enumerate(row):
                if cell == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = []

            for i in range(len(heights) + 1):
                while stack and ( i == len(heights) or heights[stack[-1]] > heights[i] ):
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

        return max_area
