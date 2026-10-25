class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        total = sum(nums)
        n = len(nums)

        current = sum(i * num for i, num in enumerate(nums))
        answer = current
        for i in range(n - 1, 0, -1):
            current += total - n * nums[i]
            answer = max(answer, current)

        return answer
