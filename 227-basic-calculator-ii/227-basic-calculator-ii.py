class Solution:
    def calculate(self, s):
        result = 0
        last = 0
        num = 0
        sign = "+"

        for i in range(len(s)):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

                if sign == "+":
                    result += last
                    last = num

                elif sign == "-":
                    result += last
                    last = -num

                elif sign == "*":
                    last = last * num

                elif sign == "/":
                    last = int(last / num)

                sign = ch
                num = 0

        return result + last
