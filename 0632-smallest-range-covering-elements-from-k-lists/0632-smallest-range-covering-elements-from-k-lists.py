import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = []
        current_max = float('-inf')

        for i, row in enumerate(nums):
            heap.append((row[0], i, 0))
            current_max = max(current_max, row[0])

        heapq.heapify(heap)

        best = [heap[0][0], current_max]

        while True:
            min_val, r, c = heapq.heappop(heap)

            if current_max - min_val < best[1] - best[0]:
                best = [min_val, current_max]

            if c + 1 == len(nums[r]):
                break

            next_val = nums[r][c + 1]
            heapq.heappush(heap, (next_val, r, c + 1))
            current_max = max(current_max, next_val)

        return best
