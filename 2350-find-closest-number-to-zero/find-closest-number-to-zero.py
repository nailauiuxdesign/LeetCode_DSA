class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_n = nums[0]  # Initialize with the first element

        for i in nums:
            if abs(i) < abs(closest_n):
                closest_n = i
            elif abs(i) == abs(closest_n) and i > closest_n:
                closest_n = i
        
        return closest_n
 