class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        for i in range(n):
            for num in reversed(result.copy()):
                result.append(num | (1 << i))
        return result
