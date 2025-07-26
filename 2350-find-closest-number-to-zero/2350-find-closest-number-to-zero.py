class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
        
        if closest < 0:
            return -closest if -closest in nums else closest
        else:
            return closest





        # closest_n = nums[0]
        # for i in nums:
        #     if abs(i) < abs(closest_n):
        #         closest_n = i
        # if closest_n < 0 and abs(closest_n) in nums:
        #     return abs(closest_n)
        # else:
        #     return closest_n
 