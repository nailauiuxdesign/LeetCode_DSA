class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0  # Left pointer of the sliding window
        longest = 0  # Track longest substring length
        r = set()  # Store unique characters            

        for right in range(len(s)): # Right pointer of the window, length of the string
            while s[right] in r: # If duplicate found
                r.remove(s[left]) # Remove leftmost character
                left += 1  # Move left pointer

            longest = max(longest, (right - left) + 1)  # Update max length
            r.add(s[right])  # Add current character to the set

        return longest # Return the longest substring length

# Time Complexity: O(n)
# Space Complexity: O(n)
