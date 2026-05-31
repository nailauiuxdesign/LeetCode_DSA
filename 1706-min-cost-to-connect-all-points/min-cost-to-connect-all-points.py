import math

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        min_dist = [math.inf] * n
        total_cost = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                distance = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                min_dist[j] = min(min_dist[j], distance)
                if min_dist[j] < min_dist[i + 1]:
                    points[j], points[i + 1] = points[i + 1], points[j]
                    min_dist[j], min_dist[i + 1] = min_dist[i + 1], min_dist[j]

            total_cost += min_dist[i + 1]

        return total_cost