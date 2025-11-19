class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for x in nums:
            n ^= x
        return n
