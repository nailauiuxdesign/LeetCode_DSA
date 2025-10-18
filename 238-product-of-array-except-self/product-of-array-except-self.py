class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # prefix product
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        
        # suffix product
        suffix = 1  
        for i, num in reversed(list(enumerate(nums))):
            res[i] *= suffix
            suffix *= num

        return res