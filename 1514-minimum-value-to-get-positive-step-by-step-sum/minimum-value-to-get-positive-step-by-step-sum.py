class Solution:
    def minStartValue(self, nums):
        total = 0
        lowest = 0

        for num in nums:
            total += num
            if total < lowest:
                lowest = total

        return 1 - lowest