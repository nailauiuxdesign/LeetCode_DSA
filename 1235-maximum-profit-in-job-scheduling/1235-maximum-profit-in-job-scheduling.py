import heapq
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        heap = [] 
        best_profit = 0

        for start, end, money in jobs:
            while heap and heap[0][0] <= start:
                best_profit = max(best_profit, heapq.heappop(heap)[1])
            heapq.heappush(heap, (end, best_profit + money))
            
        while heap:
            best_profit = max(best_profit, heapq.heappop(heap)[1])

        return best_profit
