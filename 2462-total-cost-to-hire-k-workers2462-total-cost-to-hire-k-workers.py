import heapq
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        left, right = [], []
        i, j = 0, len(costs) - 1
        total = 0
        for _ in range(k):
            while len(left) < candidates and i <= j:
                heapq.heappush(left, costs[i])
                i += 1

            while len(right) < candidates and i <= j:
                heapq.heappush(right, costs[j])
                j -= 1

            if not right or (left and left[0] <= right[0]):
                total += heapq.heappop(left)
            else:
                total += heapq.heappop(right)

        return total
