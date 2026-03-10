class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        seen = {}
        count = 0

        for num in nums:
            target = k - num
            if seen.get(target, 0) > 0:
                count += 1
                seen[target] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return count
