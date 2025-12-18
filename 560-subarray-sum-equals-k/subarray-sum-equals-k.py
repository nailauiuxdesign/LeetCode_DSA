class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        count = collections.Counter({0: 1})

        for n in nums:
            prefix_sum += n
            res += count[prefix_sum - k]
            count[prefix_sum] += 1

        return res