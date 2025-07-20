class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = s.lower()  # Convert the entire string to lowercase for case-insensitive comparison
        l, r = 0, len(s) - 1  # Initialize two pointers: left (l) at start, right (r) at end

        while l < r:  # Loop until the two pointers meet or cross
            if not s[r].isalnum():  # If the right character is not alphanumeric, skip it
                r -= 1
                continue

            if not s[l].isalnum():  # If the left character is not alphanumeric, skip it
                l += 1
                continue

            if s[r].lower() != s[l].lower():  # If the characters at left and right pointers don't match
                return False  # It's not a palindrome

            l += 1  # Move left pointer forward
            r -= 1  # Move right pointer backward

        return True   # All characters matched; it's a palindrome



        # Time O(n)
        # Space O(1)
