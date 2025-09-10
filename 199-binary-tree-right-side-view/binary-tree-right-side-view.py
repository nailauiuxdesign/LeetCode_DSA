# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = collections.deque([root])   # queue for BFS

        while q:                        # while there are nodes to process
            size = len(q)                 # number of nodes at this level
            for i in range(size):
                root = q.popleft()          # take the next node in the level
                if i == size - 1:           # last node in this level → right view
                    ans.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)

        return ans