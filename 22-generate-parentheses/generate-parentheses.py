class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, stack = [], []
 
        def backtrack(openN, closeN):
            if len(stack) == 2 * n:
                ans.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
 
            if openN > closeN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
 
        backtrack(0, 0)
        return ans