class Solution:
    def findLength(self, nums1, nums2):
        dp = [0] * (len(nums2) + 1)
        ans = 0

        for a in reversed(nums1):
            for j, b in enumerate(nums2):
                dp[j] = dp[j + 1] + 1 if a == b else 0
                ans = max(ans, dp[j])

        return ans
 