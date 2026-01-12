class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        ans = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                tank = 0
                ans = i + 1

        return ans if total >= 0 else -1
