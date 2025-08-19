class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set(nums)
        
        return len(Set) != len(nums)
