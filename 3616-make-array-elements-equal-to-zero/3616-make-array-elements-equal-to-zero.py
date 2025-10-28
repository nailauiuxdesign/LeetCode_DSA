class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        prefix = 0
        suffix = sum(nums)

        for i, num in enumerate(nums):
            suffix -= num
            prefix += num
            if num > 0:
                continue
            if prefix == suffix:
                res += 2
            if abs(prefix - suffix) == 1:
                res += 1 
        return res
