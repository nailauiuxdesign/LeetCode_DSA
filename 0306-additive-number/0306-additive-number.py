class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def check(a, b, index):
            while index < n:
                c = a + b
                c_str = str(c)
                if not num.startswith(c_str, index):
                    return False
                index += len(c_str)
                a, b = b, c
            return True

        for i in range(n):
            if num[0] == "0" and i > 0:
                break
            first = int(num[:i + 1])
            for j in range(i + 1, n - 1):

                if num[i + 1] == "0" and j > i + 1:
                    break
                second = int(num[i + 1:j + 1])
                if check(first, second, j + 1):
                    return True

        return False