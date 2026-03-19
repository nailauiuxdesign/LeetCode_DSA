import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        heap = []
        total = 0
        ans = 0

        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            total += n1

            if len(heap) > k:
                total -= heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans, total * n2)

        return ans