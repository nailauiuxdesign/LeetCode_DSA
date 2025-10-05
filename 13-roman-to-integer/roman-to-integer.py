class Solution:
    def romanToInt(self, s: str) -> int:
        summ = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                summ -= roman[a]
            else:
                summ += roman[a]

        return summ + roman[s[-1]]