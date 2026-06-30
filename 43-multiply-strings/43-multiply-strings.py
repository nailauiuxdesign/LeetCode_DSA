class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while result[-1] == 0:
            result.pop()

        answer = ""
        for digit in reversed(result):
            answer += str(digit)

        return answer
