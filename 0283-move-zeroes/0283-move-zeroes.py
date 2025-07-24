class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0  # Pointer to track position for the next non-zero element

        # Traverse the list with right pointer
        for r, value in enumerate(nums):
            if value != 0:
                nums[l], nums[r] = nums[r], nums[l]  # Swap non-zero to the front
                l += 1  # Move left pointer to next position

        return nums  # Modified list with all non-zeros moved to the front

