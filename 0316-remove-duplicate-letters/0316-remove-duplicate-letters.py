class Solution:
    def removeDuplicateLetters(self, s):
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i in range(len(s)):
            c = s[i]
            if c in seen:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)

        return "".join(stack)