class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []

        for p in parts:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "" and p != ".":
                stack.append(p)

        return "/" + "/".join(stack)