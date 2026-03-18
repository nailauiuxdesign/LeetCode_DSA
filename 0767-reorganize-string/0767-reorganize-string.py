from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, ch) for ch, count in Counter(s).items()]
        heapq.heapify(heap)
        if -heap[0][0] > (len(s) + 1) // 2:
            return ""
        res = []
        prev = (0, "")
        while heap:
            count, ch = heapq.heappop(heap)
            res.append(ch)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (count + 1, ch)

        return "".join(res)