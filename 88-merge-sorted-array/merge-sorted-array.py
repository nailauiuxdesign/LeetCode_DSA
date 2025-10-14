class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b = m-1, n-1
 
        for k in range(m + n - 1, -1, -1):
            if a < 0:
                nums1[k] = nums2[b]
                b -= 1
            elif b < 0:
                break
            elif nums1[a] > nums2[b]:
                nums1[k] = nums1[a]
                a -= 1
            else:
                nums1[k] = nums2[b]
                b -= 1