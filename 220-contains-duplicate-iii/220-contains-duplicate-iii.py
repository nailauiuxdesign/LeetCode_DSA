class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: list[int],
        indexDiff: int,
        valueDiff: int,
    ) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        bucket = {}
        size = valueDiff + 1

        for i, num in enumerate(nums):
            key = num // size
            if key in bucket:
                return True
            if key - 1 in bucket and abs(num - bucket[key - 1]) <= valueDiff:
                return True
            if key + 1 in bucket and abs(num - bucket[key + 1]) <= valueDiff:
                return True
            bucket[key] = num
            if i >= indexDiff:
                old = nums[i - indexDiff]
                del bucket[old // size]

        return False
