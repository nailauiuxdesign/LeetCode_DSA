class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[0] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]