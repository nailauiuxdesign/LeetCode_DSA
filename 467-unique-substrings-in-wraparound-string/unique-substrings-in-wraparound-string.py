class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        longest = [0] * 26
        current_length = 0

        for i in range(len(s)):
            if i > 0 and (
                ord(s[i]) == ord(s[i - 1]) + 1 or
                (s[i - 1] == "z" and s[i] == "a")
            ):
                current_length += 1
            else:
                current_length = 1

            index = ord(s[i]) - ord("a")
            longest[index] = max(longest[index], current_length)

        return sum(longest)