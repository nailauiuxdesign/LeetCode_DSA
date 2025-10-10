class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0
 
        for num in nums:
            if count == 0:
                element = num
            
            count += (1 if num == element else -1)
        
        return element