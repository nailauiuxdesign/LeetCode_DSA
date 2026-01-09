from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a = [0] * len(nums)
        self.merge_sort(nums, a, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums: List[int], a: List[int], left: int, right: int) -> None:
        if left >= right:
            return

        mid = (left + right) // 2
        self.merge_sort(nums, a, left, mid)
        self.merge_sort(nums, a, mid + 1, right)
        self.merge(nums, a, left, mid, right)

    def merge(self, nums: List[int], a: List[int], left: int, mid: int, right: int) -> None:
        for i in range(left, right + 1):
            a[i] = nums[i]

        i, j = left, mid + 1

        for k in range(left, right + 1):
            if i > mid:
                nums[k] = a[j]
                j += 1
            elif j > right:
                nums[k] = a[i]
                i += 1
            elif a[i] <= a[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = a[j]
                j += 1
