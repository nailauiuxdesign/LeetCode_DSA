from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque([root])
        res = []

        while q:
            level = []
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            res.append(level)

        return res


