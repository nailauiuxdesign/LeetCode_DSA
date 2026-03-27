class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = int(str(x)[::-1]) * sign

        if rev < MIN_INT or rev > MAX_INT:
            return 0

        return rev