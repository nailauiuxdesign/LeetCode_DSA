class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = float('inf')
 
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
 
            l, r = i + 1, n - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
 
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
 
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    l += 1
                else:
                    r -= 1
 
        return closest_sum