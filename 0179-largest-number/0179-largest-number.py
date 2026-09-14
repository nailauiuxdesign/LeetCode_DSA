from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1

        nums.sort(key=cmp_to_key(compare))
        return ''.join(nums).lstrip('0') or '0'