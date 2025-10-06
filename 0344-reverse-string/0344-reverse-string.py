class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            # Swap characters
            s[l], s[r] = s[r], s[l]
            
            # Move pointers
            l += 1
            r -= 1