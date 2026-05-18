class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(
            self.houseRobber(nums[1:]),
            self.houseRobber(nums[:-1])
        )

    def houseRobber(self, nums):
        prev = 0
        curr = 0
        for money in nums:
            temp = max(curr, prev + money)
            prev = curr
            curr = temp

        return curr