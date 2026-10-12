class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1

        while place <= n:
            divisor = place * 10
            higher = n // divisor
            current = (n // place) % 10
            lower = n % place

            count += higher * place
            if current == 1:
                count += lower + 1
            elif current > 1:
                count += place
            place *= 10

        return count