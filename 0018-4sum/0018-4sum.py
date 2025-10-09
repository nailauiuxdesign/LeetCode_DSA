class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(l, r, target, k):
            res = []
            if r - l + 1 < k or k < 2 or target < nums[l] * k or target > nums[r] * k:
                return res

            if k == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append([nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
                return res

            for i in range(l, r + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue
                for subset in kSum(i + 1, r, target - nums[i], k - 1):
                    res.append([nums[i]] + subset)
            return res

        nums.sort()
        return kSum(0, len(nums) - 1, target, 4)
