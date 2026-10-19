
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        factorial = [1] * (n + 1)

        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        k -= 1
        result = ""

        for i in range(n - 1, -1, -1):
            index = k // factorial[i]
            k %= factorial[i]
            result += str(nums.pop(index))

        return result
