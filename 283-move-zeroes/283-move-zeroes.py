class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0  # Pointer to track the position to place the next non-zero element

        # Move all non-zero elements to the front
        for r in nums:
            if r != 0:
                nums[l] = r
                l += 1

        # Fill the rest of the list with zeros
        for i in range(l, len(nums)):
            nums[i] = 0

