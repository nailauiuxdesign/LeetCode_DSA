class Solution:
  def pivotIndex(self, nums: list[int]) -> int:
    right_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
      if left_sum == right_sum - left_sum - num:
        return i
      left_sum += num
    return -1