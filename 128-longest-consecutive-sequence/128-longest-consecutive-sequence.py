class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0
        for num in mySet:
            if (num - 1) not in mySet: # 100 pre 9
                length = 0
                curr = num
                while curr in mySet:
                    curr += 1
                    length += 1
                longest = max(length, longest)
        return longest
