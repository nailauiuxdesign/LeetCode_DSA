class Solution:
    def isHappy(self, n: int) -> bool:      
        def square_sum(num):
            total = 0
            while num:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = square_sum(n)

        return n == 1