class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(text):
            count = 0

            for char in text:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1

                if count < 0:
                    return False
            return count == 0

        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        result = []
        def backtrack(text, start, left, right):
            if left == 0 and right == 0:
                if is_valid(text):
                    result.append(text)
                return
            for i in range(start, len(text)):
                if i > start and text[i] == text[i - 1]:
                    continue
                if text[i] == '(' and left > 0:
                    backtrack(text[:i] + text[i + 1:], i, left - 1, right)
                elif text[i] == ')' and right > 0:
                    backtrack(text[:i] + text[i + 1:], i, left, right - 1)

        backtrack(s, 0, left, right)
        return result