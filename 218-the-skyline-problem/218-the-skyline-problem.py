class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        if not buildings:
            return []

        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        left_height = right_height = 0

        def add_point(x, height):
            if result and result[-1][0] == x:
                result[-1][1] = height
            elif not result or result[-1][1] != height:
                result.append([x, height])

        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x, left_height = left[i]
                i += 1
            elif right[j][0] < left[i][0]:
                x, right_height = right[j]
                j += 1
            else:
                x = left[i][0]
                left_height = left[i][1]
                right_height = right[j][1]
                i += 1
                j += 1

            add_point(x, max(left_height, right_height))

        while i < len(left):
            add_point(*left[i])
            i += 1

        while j < len(right):
            add_point(*right[j])
            j += 1

        return result
