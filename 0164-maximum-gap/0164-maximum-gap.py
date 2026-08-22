class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        low = min(nums)
        high = max(nums)

        if low == high:
            return 0

        n = len(nums)
        gap = (high - low + n - 2) // (n - 1)
        buckets = [[float("inf"), float("-inf")] for _ in range(n)]

        for num in nums:
            i = (num - low) // gap
            buckets[i][0] = min(buckets[i][0], num)
            buckets[i][1] = max(buckets[i][1], num)

        answer = 0
        previous = low

        for bucket_min, bucket_max in buckets:
            if bucket_min == float("inf"):
                continue
            answer = max(answer, bucket_min - previous)
            previous = bucket_max

        return answer