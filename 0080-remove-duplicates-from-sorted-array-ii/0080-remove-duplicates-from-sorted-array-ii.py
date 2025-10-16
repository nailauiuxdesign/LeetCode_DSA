class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 2

        for i in range (2, len(nums)):
            if nums [i] != nums[c - 2]:
                nums[c] = nums[i]
                c += 1

        return c
