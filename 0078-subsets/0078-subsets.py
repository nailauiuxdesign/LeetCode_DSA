class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, s = [], []
 
        def backtrack(i):
            if i == n:
                res.append(s[:])
                return
 
            backtrack(i + 1) # Don't pick nums[i]
 
            s.append(nums[i]) # Pick nums[i]
            backtrack(i + 1)
            s.pop()
 
        backtrack(0)
        return res