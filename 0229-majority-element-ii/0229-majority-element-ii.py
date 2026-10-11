class Solution:
    def majorityElement(self, nums):
        first = second = None
        count1 = count2 = 0

        for num in nums:
            if num == first:
                count1 += 1
            elif num == second:
                count2 += 1
            elif count1 == 0:
                first = num
                count1 = 1
            elif count2 == 0:
                second = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        count1 = count2 = 0
        for num in nums:
            if num == first:
                count1 += 1
            elif num == second:
                count2 += 1
        if count1 > len(nums) // 3:
            result.append(first)
        if count2 > len(nums) // 3:
            result.append(second)

        return result