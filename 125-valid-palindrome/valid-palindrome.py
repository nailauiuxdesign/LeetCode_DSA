class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1           # Left pointer starting from 0, Right pointer starting from the end

        while l < r:        # Loop until the pointers meet
            if not s[r].isalnum():   # Skip non-alphanumeric characters on the left
                r -= 1
                continue

            if not s[l].isalnum():   # Skip non-alphanumeric characters on the right
                l += 1
                continue

            if s[r].lower() != s[l].lower():  # Compare characters in a case-insensitive manner
                return False                  # If mismatch, it's not a palindrome

            r -= 1    # Move right pointer to the left
            l += 1    # Move left pointer to the right

        return True   # All characters matched; it's a palindrome

        # Time O(n)
        # Space O(1)
