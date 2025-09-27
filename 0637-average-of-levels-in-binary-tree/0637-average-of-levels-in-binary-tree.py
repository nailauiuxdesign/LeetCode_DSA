# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        que = deque()
        que.append(root)
 
        while que:
            level_sum = 0
            level_size = len(que)
            for _ in range(level_size):
                node = que.popleft()
                level_sum += node.val
 
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
 
            avg.append(level_sum / level_size)
        
        return avg