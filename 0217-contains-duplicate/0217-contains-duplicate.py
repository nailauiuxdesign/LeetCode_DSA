class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = set()
        for num in nums:
            if num in i:
                return True
            else:
                i.add(num)
        return False