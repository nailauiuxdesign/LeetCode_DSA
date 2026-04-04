import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.next_num = 1
        self.min_heap = []
        self.used = set()

    def popSmallest(self) -> int:
        if self.min_heap:
            val = heapq.heappop(self.min_heap)
            self.used.remove(val)
            return val

        val = self.next_num
        self.next_num += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.used:
            heapq.heappush(self.min_heap, num)
            self.used.add(num)