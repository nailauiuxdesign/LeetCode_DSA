
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        start = 0
        for i, char in enumerate(s):
            if char == '[':
                stack.append(NestedInteger())
                start = i + 1
            elif char in ',]':
                if i > start:
                    stack[-1].add(NestedInteger(int(s[start:i])))
                start = i + 1
                if char == ']':
                    current = stack.pop()
                    if stack:
                        stack[-1].add(current)
                    else:
                        return current
