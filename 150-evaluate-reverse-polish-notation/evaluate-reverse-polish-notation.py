class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }

        for t in tokens:
                if t in op:
                    b = stk.pop()
                    a = stk.pop()
                    stk.append(op[t](a, b))
                else:
                    stk.append(int(t))

        return stk.pop()