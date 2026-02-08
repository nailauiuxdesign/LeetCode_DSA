from collections import deque
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        cost = 0
        week = deque()
        month = deque()

        for d in days:
            while week and week[0][0] + 7 <= d:
                week.popleft()
            while month and month[0][0] + 30 <= d:
                month.popleft()

            week.append((d, cost + costs[1]))
            month.append((d, cost + costs[2]))

            cost = min(
                cost + costs[0],
                week[0][1],
                month[0][1]
            )

        return cost
