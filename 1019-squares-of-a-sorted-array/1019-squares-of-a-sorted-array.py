class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l = 0
        # r = len(nums) - 1
        # ans = []
 
        # while l <= r:
        #     if abs(nums[l]) > abs(nums[r]):
        #         ans.append(nums[l] ** 2)
        #         l += 1
        #     else:
        #         ans.append(nums[r] ** 2)
        #         r -= 1
 
        # ans.reverse()
 
        # return ans
        n = len(nums)
        l = 0
        r = n - 1
        ans = [0] * n

        while n:
            n -= 1
            if abs(nums[l]) > abs(nums[r]):
                ans[n] = nums[l] * nums[l]
                l += 1
            else:
                ans[n] = nums[r] * nums[r]
                r -= 1

        return ans