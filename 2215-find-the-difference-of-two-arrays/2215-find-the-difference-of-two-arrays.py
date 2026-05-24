class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        only_in_nums1 = []
        for num in set1:
            if num not in set2:
                only_in_nums1.append(num)
            else:
                set2.remove(num)
        return [only_in_nums1, list(set2)]
