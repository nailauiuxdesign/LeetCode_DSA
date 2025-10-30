class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate (heights):
            start = i # start from index
            while stack and stack[-1][1] > h: #stack and top of stack [-1][1]
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # i - index = width
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea