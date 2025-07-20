class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for e in nums[0::]:  # Loop through a copy of the list
            nums.append(e)   # Add each item to the end
        return nums          # Return the extended list
