class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            value = divisor
            count = 1
            while dividend >= value << 1:
                value <<= 1
                count <<= 1
            dividend -= value
            result += count

        if negative:
            result = -result

        return result
