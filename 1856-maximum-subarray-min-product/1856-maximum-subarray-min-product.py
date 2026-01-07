import itertools

class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        prefix = list(itertools.accumulate(nums, initial=0))
        stack = []
        res = 0

        for i in range(len(nums) + 1):
            while stack and (i == len(nums) or nums[stack[-1]] > nums[i]):
                idx = stack.pop()
                left = stack[-1] + 1 if stack else 0
                total = prefix[i] - prefix[left]
                res = max(res, nums[idx] * total)

            stack.append(i)

        return res % MOD
