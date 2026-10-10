from functools import lru_cache
class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> list[int]:
        results = []

        for i, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for a in left:
                    for b in right:
                        if char == "+":
                            results.append(a + b)
                        elif char == "-":
                            results.append(a - b)
                        else:
                            results.append(a * b)

        if not results:
            return [int(expression)]

        return results