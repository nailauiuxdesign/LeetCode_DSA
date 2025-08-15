# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  
        if not root: return 0

        i = collections.deque()
        level = 1
        i.append((root, level))

        while i:
            currentNode, currentLevel = i.popleft()
            if currentNode.left:
                i.append((currentNode.left, currentLevel+1))
            if currentNode.right:
                i.append((currentNode.right, currentLevel+1))
            level = max(level, currentLevel)

        return level

