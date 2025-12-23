class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m

        while True:
            i = (l + r) // 2
            j = half - i

            left_A  = A[i - 1] if i > 0 else float('-inf')
            right_A = A[i]     if i < m else float('inf')
            left_B  = B[j - 1] if j > 0 else float('-inf')
            right_B = B[j]     if j < n else float('inf')

            if left_A <= right_B and left_B <= right_A:
                if total % 2:
                    return min(right_A, right_B)
                return (max(left_A, left_B) + min(right_A, right_B)) / 2

            elif left_A > right_B:
                r = i - 1
            else:
                l = i + 1
