class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [1] * n
        postfix = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Calculate postfix products
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # Final result
        for i in range(n):
            res[i] = prefix[i] * postfix[i]

        return res

        
        
        # n = len(nums)
        # res=[0] * n
        # prefix = [1]*n #[1,1,2,8]
        # #cal left product
        # for i in range(1, len(nums)): i=2
        #     prefix[i] = prefix[i-1]*nums[i-1]
        # postfix = [1]*n #[48,24,6,1]

        # #cal right prod
        # for i in range(n-2,-1,-1): i=0
        #     postfix[i] = nums[i+1]*postfix[i+1]
        # for i in range(n):
        #     res[i] = prefix[i]*postfix[i]
        # return res