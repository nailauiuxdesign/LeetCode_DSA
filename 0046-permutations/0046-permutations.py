class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, s = [], []
 
        def backtrack():
            if len(s) == n:
                res.append(s[:])
                return
 
            for x in nums:
                if x not in s:
                    s.append(x)
                    backtrack()
                    s.pop()
 
        backtrack()
        return res